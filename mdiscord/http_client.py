from typing import Dict
from mdiscord.base_model import Snowflake
from mdiscord.endpoints import Endpoints
import aiohttp

class HTTP_Client(Endpoints):
    token: str
    user_id: Snowflake
    _session: aiohttp.ClientSession
    lock: Dict[str, bool]
    def __init__(self, token=None, user_id=None) -> None:
        self.token=token
        self.user_id = user_id
        self.lock = {"global": False}
        self._new_session()
        super().__init__()
    
    def _new_session(self):
        import platform
        if 'linux' in platform.system().lower():
            from aiohttp.resolver import AsyncResolver
            resolver = AsyncResolver(nameservers=['8.8.8.8', '8.8.4.4'])
        else:
            resolver = None        
        self._session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False, resolver=resolver))#, json_serialize=Encoder().encode)
    
    def _prepare_payload(self, **kwargs):
        if 'headers' not in kwargs:
            kwargs['headers'] = []
        if self.token:
            kwargs['headers'].append(("Authorization", f"Bot {self.token}"))
        if kwargs.get('reason'):
            kwargs['headers'].append(("X-Audit-Log-Reason", kwargs.pop('reason')))
        if not kwargs.get('file'):
            kwargs['headers'].append(("Content-Type", "application/json"))
        else:
            kwargs['data'] = aiohttp.FormData()
            import ujson as json
            kwargs['data'].add_field("payload_json", json.dumps(kwargs["json"]))
            kwargs['data'].add_field("file", kwargs["file"],
                filename=kwargs["filename"],
                content_type="application/octet-stream"
            )
            kwargs.pop('json')

        kwargs = self._serialize(**kwargs)
        return kwargs

    def _serialize(self, **kwargs):
        from mlib.utils import remove_None
        if kwargs.get('json'):
            from .serializer import as_dict
            kwargs['json'] = as_dict(kwargs['json'])
            kwargs['json'] = remove_None(kwargs.get('json',{}))
        if kwargs.get('params'):
            kwargs["params"] = remove_None(kwargs.get("params"))
            for param in kwargs["params"]:
                kwargs["params"][param] = str(kwargs["params"][param])
            for i in ["before", "after", "between"]:
                if kwargs["params"].get(i, False) is None:
                    kwargs.pop(i)
        kwargs.pop('filename', None)
        kwargs.pop('file', None)
        kwargs = remove_None(kwargs)
        return kwargs

    async def api_call(self, path: str, method: str, **kwargs):
        kwargs = self._prepare_payload(**kwargs)
        return await self._api_call(path, method, **kwargs)
    
    async def _api_call(self, path: str, method: str="GET", **kwargs):
        import asyncio
        try:
            bucket = path.split('/', 3)[2]
        except:
            bucket = None
        if not (self.lock.get(bucket, False) is False and self.lock.get('global') is False):
            if 'reaction' in path:
                await asyncio.sleep(0.5)
            await asyncio.sleep(0.75)
            return await self._api_call(path, method, **kwargs)

        from mdiscord.base_model import BASE_URL
        async with self._session.request(method, BASE_URL+"api"+path, **kwargs) as res:
            from mdiscord.models import HTTP_Response_Codes
            from mdiscord.exceptions import BadRequest, RequestError, JsonBadRequest, NotFound

            try:
                res.raise_for_status()
            except Exception as ex:
                print(ex)

            if res.ok:
                if res.status == HTTP_Response_Codes.NO_CONTENT.value:
                    return None
                try:
                    r = await res.json()
                except Exception as ex:
                    raise RequestError(f"Error sending request: [{res.reason}]: [{method}] {path}")

                if 'message' in r:
                    raise JsonBadRequest(f"[{res.reason}] [{r['code']}] - {r['message']}: [{method}] {path}", r.get('errors','') if 'errors' in r else None)
                if type(r) is dict:
                    return dict({"_Client": self}, **r)
                return list(dict({"_Client":self}, **i) for i in r)
            elif res.status == HTTP_Response_Codes.BAD_REQUEST.value:
                raise BadRequest(f"[{res.reason}] {await res.text()}", f"[{method}] {path}")
            elif res.status == HTTP_Response_Codes.NOT_FOUND.value:
                raise NotFound(f"[{res.reason}] {await res.text()}", f"[{method}] {path}")

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
                return await self._api_call(path, method, **kwargs)
            
            elif res.status >= 500:
                await asyncio.sleep(1)
                return await self._api_call(path, method, **kwargs)
            res.raise_for_status()

    async def close(self):
        await self._session.close()
