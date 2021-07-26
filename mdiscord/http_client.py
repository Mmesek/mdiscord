import aiohttp
from typing import Dict

from mdiscord.base_model import Snowflake
from mdiscord.endpoints import Endpoints
from mdiscord.serializer import Serializer

class HTTP_Client(Endpoints, Serializer):
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
            except aiohttp.ClientResponseError as ex:
                import ujson
                error_message = ujson.loads(res.content._buffer.popleft())
                if res.status == HTTP_Response_Codes.BAD_REQUEST.value:
                    raise BadRequest(f"[{res.reason}] {error_message.get('message', error_message)}", f"[{method}] {path}")
                elif res.status == HTTP_Response_Codes.NOT_FOUND.value:
                    raise NotFound(f"[{res.reason}] {error_message.get('message', error_message)}", f"[{method}] {path}")

                elif res.status == HTTP_Response_Codes.TOO_MANY_REQUESTS.value:
                    is_global = res.headers.get('X-RateLimit-Global') is True
                    #TODO: Actual ratelimiter, get reset and remaining from headers, put into local dict (as tuple of remaining, reset?)
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
