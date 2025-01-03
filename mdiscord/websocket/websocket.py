# -*- coding: utf-8 -*-
"""
API Client
----------

Websocket Client for Discord API.

:copyright: (c) 2021 Mmesek
"""

import asyncio
import time

from mlib.types import Invalid

from mdiscord import types as objects
from mdiscord.http.client import HTTP_Client
from mdiscord.utils.serializer import Deserializer, as_dict
from mdiscord.utils.utils import log
from mdiscord.websocket.opcodes import Gateway_Opcodes, Opcodes


class WebSocket_Client(HTTP_Client, Opcodes):
    username: str = "[NOT CONNECTED]"
    latency: float = 0.0
    presence: objects.Gateway_Presence_Update = None
    intents: int = 0
    decompress: Deserializer = None

    def __init__(self, name: str, cfg: dict, shard: int = 0, total_shards: int = 1):
        self.username = "[NOT CONNTECTED] " + name
        self.cfg = cfg

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
        log.debug("Initating Bot with token %s[...]%s", self.token[:5], self.token[-5:])

    async def init(self):
        """Feel free to overwrite this method to perform any async initialization that needs to happen"""
        pass

    async def __aenter__(self):
        self.decompress = Deserializer()
        if self._session and self._session.closed or not self._session:
            log.debug("Restarting session")
            self._new_session()
        if not self.resume_url:
            gate = await self.get_gateway_bot()
            url = gate.url
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
                    if data.op != Gateway_Opcodes.HEARTBEAT_ACK and data.s is not None:
                        self.last_sequence = data.s
                    asyncio.create_task(self.opcodes.get(data.op.value, Invalid)(data), name="Dispatch")
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

    @classmethod
    async def runner(cls, **kwargs):
        ws = cls(**kwargs)
        await ws.init()
        while True:
            async with ws:
                try:
                    await ws.receive()
                except KeyboardInterrupt:
                    return
                except Exception as ex:
                    log.critical("Uncaught Exception", exc_info=ex)

    @classmethod
    def run(cls, **kwargs):
        asyncio.run(cls.runner(**kwargs))
