import asyncio
import time

import aiohttp
import msgspec

from mdiscord.meta_types import Snowflake
from mdiscord.endpoints import Endpoints
from mdiscord.serializer import Serializer
from mdiscord.utils import log


class HTTP_Client(Endpoints, Serializer):
    token: str
    user_id: Snowflake
    _session: aiohttp.ClientSession
    lock: dict[str, bool]
    api_version: int

    def __init__(self, token=None, user_id=None, *, api_version: int = None) -> None:
        self.token = token
        self.user_id = user_id
        self.lock = {"global": False}
        self.api_version = api_version
        self._new_session()
        super().__init__()

    def _new_session(self):
        import platform

        if "linux" in platform.system().lower():
            from aiohttp.resolver import AsyncResolver

            resolver = AsyncResolver(nameservers=["8.8.8.8", "8.8.4.4"])
        else:
            resolver = None
        self._session = aiohttp.ClientSession(
            connector=aiohttp.TCPConnector(ssl=False, resolver=resolver, force_close=True, enable_cleanup_closed=True)
        )  # , json_serialize=Encoder().encode)

    async def api_call(self, path: str, method: str, **kwargs):
        kwargs = self._prepare_payload(**kwargs)
        return await self._api_call(path, method, **kwargs)

    async def _api_call(self, path: str, method: str = "GET", **kwargs):
        try:
            bucket = path.split("/", 3)[2]
        except IndexError:
            bucket = None
        limit = self.lock.get(bucket, (0, 0))
        if limit is True or self.lock.get("global", False):
            # if not (self.lock.get(bucket, False) is False and self.lock.get('global') is False):
            if "reaction" in path:
                await asyncio.sleep(0.5)
            await asyncio.sleep(0.75)
            return await self._api_call(path, method, **kwargs)
        elif time.time() < limit[1] and not limit[0]:
            log.debug("Rate Limit exhausted on bucket %s. Sleeping for %s", bucket or "GLOBAL", limit[1] - time.time())
            await asyncio.sleep(limit[1] - time.time())

        from mdiscord.base_model import BASE_URL

        async with self._session.request(
            method, BASE_URL + "api" + (f"/v{self.api_version}" if self.api_version else "") + path, **kwargs
        ) as res:
            from mdiscord.models import HTTP_Response_Codes
            from mdiscord.exceptions import BadRequest, NotFound
            from .serializer import from_builtins

            r = await res.text(encoding="utf-8")
            if res.headers.get("content-type", None) == "application/json":
                r = msgspec.json.decode(r, dec_hook=from_builtins)

            self.lock[bucket] = (
                int(res.headers.get("X-RateLimit-Remaining", 1)),
                float(res.headers.get("X-RateLimit-Reset", 0)),
            )

            if res.status == HTTP_Response_Codes.NO_CONTENT.value:
                return None

            elif res.status == HTTP_Response_Codes.BAD_REQUEST.value:
                raise BadRequest(
                    reason=res.reason,
                    msg=r.get("message", r),
                    method=method,
                    path=path,
                    payload=kwargs.get("json"),
                    errors=r.get("errors", {}),
                )

            elif res.status == HTTP_Response_Codes.NOT_FOUND.value:
                raise NotFound(reason=res.reason, method=method, path=path)

            elif res.status == HTTP_Response_Codes.TOO_MANY_REQUESTS.value:
                is_global = res.headers.get("X-RateLimit-Global") is True
                # TODO: Actual ratelimiter, get reset and remaining from headers, put into local dict (as tuple of remaining, reset?)

                if not is_global:
                    self.lock[bucket] = True
                else:
                    self.lock["global"] = True

                retry_after = float(res.headers.get("Retry-After", 1))

                if "reaction" in path:
                    retry_after += 0.75

                await asyncio.sleep(retry_after)

                if not is_global:
                    self.lock[bucket] = (0, 0)
                else:
                    self.lock["global"] = False

                return await self._api_call(path, method, **kwargs)

            elif res.status >= 500:
                await asyncio.sleep(1)
                return await self._api_call(path, method, **kwargs)

            if type(r) is dict:
                return dict({"_Client": self}, **r)
            return list(dict({"_Client": self}, **i) for i in r)

    async def close(self):
        await self._session.close()
