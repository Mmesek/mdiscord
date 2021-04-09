# -*- coding: utf-8 -*-
'''
API Client
----------

Discord API Client.

:copyright: (c) 2021 Mmesek

'''

import asyncio, aiohttp
from mdiscord.base_model import Snowflake
import ujson as json
from . import types as objects

from .opcodes import Opcodes
from .endpoints import Endpoints

from .serializer import Deserializer, as_dict
from .exceptions import BadRequest, RequestError, JsonBadRequest

class Client(Endpoints, Opcodes):
    username: str = "[NOT CONNECTED]"
    counters: dict = dict
    latency: float = 0.0
    presence: objects.Gateway_Status_Update = None
    alias: str = "?"
    sub: bool = False
    intents: int = 0
    emoji: dict = dict
    primary_guild: Snowflake = 463433273620824104
    def __init__(self, name: str, cfg: dict, db: object, cache: object, shard: int = 0, total_shards: int = 1):
        self.token = cfg['DiscordTokens'][name]
        self.username = '[NOT CONNTECTED] ' + name
        self.counters = {"EXECUTED_COMMANDS": 0}
        
        self.db = db
        self.cache = cache
        self.context = {"dm": {}}

        self.latency = None
        
        self.cfg = cfg

        import time
        self.presence = objects.Gateway_Status_Update(
            since= time.time(),
            activities=[objects.Bot_Activity(
                name=cfg[name].get('presence'), #"How the world burns"
                type=cfg[name].get('presence_type'), #Activity_Types.WATCHING.value
                url=cfg[name].get('url')
                )],
            status= cfg[name].get('status', objects.Status_Types.ONLINE.value),
            afk= False)

        self.alias = cfg[name].get('alias', '?')
        self.sub = cfg[name].get('subscription', False) #True
        self.intents = cfg[name].get('intents', 0) #14271 # https://ziad87.net/intents/

        self.emoji = cfg["Emoji"]
        self.primary_guild = cfg[name].get('primary_guild', 463433273620824104)
        
        self.shards = [shard, total_shards]
        self.lock = {"global": False}

        self.decompress = Deserializer()
        
        print("\nInitating Bot with token: ", self.token)

    async def _api_call(self, path: str, method: str = "GET", reason: str = None, **kwargs):
        headers = [("Authorization", f"Bot {self.token}")]
        if reason:
            headers.append(("X-Audit-Log-Reason", reason))
        def remove_None(d):
            for k, a in d.copy().items():
                if a is None:
                    d.pop(k, None)
                elif type(a) is dict:
                    d[k] = remove_None(a)
                elif type(a) is list:
                    d[k] = [remove_None(i) if type(i) is dict else i for i in a]
            return d
        if kwargs.get('json'):
            kwargs['json'] = as_dict(kwargs['json'])
            kwargs['json'] = remove_None(kwargs.get('json',{}))
#        for key, arg in kwargs.get('json',{}).copy().items():
#            if arg is None:
#                kwargs['json'].pop(key, None)
        if kwargs.get('params'):
            for param in kwargs["params"]:
                kwargs["params"][param] = str(kwargs["params"][param])
            for i in ["before", "after", "between"]: #
                if kwargs["params"].get(i, False) is None: #
                    kwargs.pop(i) #
        #TODO: kwargs to json #I think it's handled now?
        if not kwargs.get('file'):
            headers.append(("Content-Type", "application/json"))
            data = None
        else:
            data = aiohttp.FormData()
            data.add_field("payload_json", json.dumps(kwargs["json"]))
            data.add_field("file", kwargs["file"],
                filename=kwargs["filename"],
                content_type="application/octet-stream"
            )
            kwargs.pop('json')
        kwargs.pop('filename', None)
        kwargs.pop('file', None)
        res = await self._client_session.request( ##
            method, objects.BASE_URL + path,
            data=data, headers=headers, 
            **kwargs)
        if not res.ok and res.status != 403: #
            print(res.status, res.reason, path) #
        return res #

    async def api_call(self, path: str, method: str = "GET", reason: str = None, **kwargs):
        try:
            bucket = path.split('/', 3)[2]
        except:
            bucket = None

        if self.lock.get(bucket, False) is False and self.lock.get('global') is False:
            from .models import HTTP_Response_Codes
            res = await self._api_call(path, method, reason, **kwargs)
            if res.status == HTTP_Response_Codes.NO_CONTENT.value:
                return None

            elif res.status == HTTP_Response_Codes.BAD_REQUEST.value:
                raise BadRequest(f"[{res.reason}] {await res.text()}", f"[{method}] {path}")

            elif res.status == HTTP_Response_Codes.TOO_MANY_REQUESTS.value:
                is_global = res.headers.get('X-RateLimit-Global') is True
                if not is_global:
                    self.lock[bucket] = True
                else:
                    self.lock['global'] = True
                retry_after = float(res.headers.get('Retry-After', 1))
                if 'reaction' in path:
                    retry_after += 0.75
                await asyncio.sleep(retry_after / 1000 if retry_after > 3 else retry_after)
                if not is_global:
                    self.lock[bucket] = False
                else:
                    self.lock['global'] = False
                return await self.api_call(path, method, reason, **kwargs)

            elif res.status >= 500:
                await asyncio.sleep(1)
                return await self.api_call(path, method, reason, **kwargs)

            try:
                r = await res.json()
            except Exception as ex:
                raise RequestError(f"Error sending request: [{res.reason}]: [{method}] {path}")
            
            if 'message' in r:
                raise JsonBadRequest(f"[{res.reason}] [{r['code']}] - {r['message']}: [{method}] {path}", r.get('errors','') if 'errors' in r else None)
            if type(r) is dict:
                return dict({"_Client": self}, **r)
            return list(dict({"_Client":self}, **i) for i in r)

        elif 'reaction' in path:
            # Ratelimit information for them is longer/inconsitent
            # Still hits 429 hence additional sleep
            await asyncio.sleep(0.5)
        await asyncio.sleep(0.75)
        return await self.api_call(path, method, reason, **kwargs)

    async def __aenter__(self):
        self.decompress = Deserializer()

        import platform
        if 'linux' in platform.system().lower():
            from aiohttp.resolver import AsyncResolver
            resolver = AsyncResolver(nameservers=['8.8.8.8', '8.8.4.4'])
        else:
            resolver = None
        
        self._client_session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False, resolver=resolver))#, json_serialize=Encoder().encode)
        gate = await self.get_gateway_bot()
        self._ws = await self._client_session.ws_connect(f"{gate['url']}?v={self.cfg['Discord']['api_version']}&encoding=json&compress=zlib-stream")
        return self

    async def receive(self):
        async for msg in self._ws:
            try:
                data = self.decompress(msg.data)
                if data is not None:
                    if data.op != 11 and data.s is not None:
                        self.last_sequence = data.s
                    from mlib.types import Invalid
                    asyncio.create_task(self.opcodes.get(data.op, Invalid)(self, data))#, name="Dispatch")
            except Exception as ex:
                print(f"Exception! {ex}\nType: {msg.type}\nData: {msg.data}\nExtra: {msg.extra}")

    async def send(self, _json: object):
        _json = as_dict(_json)
        #TODO: json (object) to json (dict) #done?
        try: #
            return await self._ws.send_json(_json) ##
        except Exception as ex: #
            print("Send Error", ex) #

    async def __aexit__(self, *args, **kwargs):
        await asyncio.sleep(1)
        if hasattr(self, 'heartbeating'):
            self.heartbeating.cancel()
        await self._ws.close()
        await self._client_session.close()
