# -*- coding: utf-8 -*-
'''
API Client
----------

Discord API Client.

:copyright: (c) 2021 Mmesek

'''

import asyncio
from mdiscord.base_model import Snowflake
from . import types as objects
from .http_client import HTTP_Client
from .opcodes import Opcodes

from .serializer import Deserializer, as_dict

class WebSocket_Client(HTTP_Client, Opcodes):
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

        self.decompress = Deserializer()
        super().__init__(token=cfg['DiscordTokens'][name], user_id=cfg[name].get('user_id'))
        print("\nInitating Bot with token: ", self.token)

    async def __aenter__(self):
        self.decompress = Deserializer()
        
        gate = await self.get_gateway_bot()
        self._ws = await self._session.ws_connect(f"{gate['url']}?v={self.cfg['Discord']['api_version']}&encoding=json&compress=zlib-stream")
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
