# -*- coding: utf-8 -*-
"""
API Client
----------

Discord API Client.

:copyright: (c) 2021 Mmesek

"""

import asyncio
from . import types as objects
from .http_client import HTTP_Client
from .opcodes import Opcodes

from .serializer import Deserializer, as_dict
from .utils import log


class WebSocket_Client(HTTP_Client, Opcodes):
    username: str = "[NOT CONNECTED]"
    latency: float = 0.0
    presence: objects.Gateway_Presence_Update = None
    intents: int = 0
    decompress: Deserializer = None

    def __init__(self, name: str, cfg: dict, shard: int = 0, total_shards: int = 1):
        self.username = "[NOT CONNTECTED] " + name

        self.cfg = cfg

        import time

        self.presence = objects.Gateway_Presence_Update(
            since=time.time(),
            activities=[
                objects.Bot_Activity(
                    name=cfg.get(name, {}).get("presence", None),
                    type=cfg.get(name, {}).get("presence_type", None),
                    url=cfg.get(name, {}).get("url", None),
                )
            ],
            status=cfg.get(name, {}).get("status", objects.Status_Types.ONLINE),
            afk=False,
        )

        self.intents = cfg[name].get("intents", 0)
        self.shards = [shard, total_shards]

        super().__init__(
            token=cfg["DiscordTokens"][name],
            user_id=cfg[name].get("user_id"),
            api_version=cfg.get("Discord", {}).get("api_version", None),
        )
        log.debug("Initating Bot with token %s", self.token)

    async def __aenter__(self):
        self.decompress = Deserializer()
        if self._session and self._session.closed or not self._session:
            log.info("Restarting session")
            self._new_session()
        if not self.resume_url:
            gate = await self.get_gateway_bot()
            url = gate["url"]
        else:
            url = self.resume_url
        self._ws = await self._session.ws_connect(
            f"{url}?" + (f"v={self.api_version}&" if self.api_version else "") + "encoding=json&compress=zlib-stream"
        )
        return self

    async def receive(self):
        async for msg in self._ws:
            try:
                data = self.decompress(msg.data)
                if data is not None:
                    if data.op != 11 and data.s is not None:
                        self.last_sequence = data.s
                    from mlib.types import Invalid

                    asyncio.create_task(self.opcodes.get(data.op, Invalid)(data), name="Dispatch")
            except Exception as ex:
                log.exception("Exception! Type: %s", msg.type, exc_info=ex)

    async def send(self, _json: object):
        _json = as_dict(_json)
        try:  #
            return await self._ws.send_json(_json)  ##
        except Exception as ex:  #
            log.exception("Send Error", exc_info=ex)

    async def __aexit__(self, *args, **kwargs):
        await asyncio.sleep(1)
        if hasattr(self, "heartbeating"):
            self.heartbeating.cancel()
            self.keepConnection = False
        await self._ws.close()
        await self._session.close()
