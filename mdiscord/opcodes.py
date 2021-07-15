# -*- coding: utf-8 -*-
'''
Discord Opcodes
----------

Discord API Opcodes.

:copyright: (c) 2020 Mmesek

'''
import asyncio, time
import sys, traceback, platform
from typing import List, Optional
from collections import Counter

from .types import (
    Gateway_Events, 
    Gateway_Payload, 
    Gateway_Opcodes,
    Gateway_Presence_Update,
    Gateway_Voice_State_Update,
    Identify, Resume,
    Guild_Request_Members,
    Snowflake,
    Status_Types, Activity_Types,
    Bot_Activity
)
from .utils import log
from .exceptions import BadRequest, JsonBadRequest, Insufficient_Permissions, NotFound
from mlib.types import Invalid, aInvalid
Dispatch = {}

class Opcodes:
    counters: Counter = Counter()
    keepConnection: bool = True
    latency: float = 0.0
    heartbeat_sent: float = 0.0
    heartbeating: asyncio.Task

    async def dispatch(self, data: Gateway_Payload) -> None:
        data.d = getattr(Gateway_Events, data.t.title(), Invalid)(_Client=self, **data.d)
        if not getattr(data.d, 'guild_id', False) and 'MESSAGE' in data.t:
            data.t = 'DIRECT_'+data.t
        if getattr(data.d, 'is_bot', False):
            return
        self.counters[data.t] += 1
        for priority in sorted(Dispatch.get(data.t, {})):
            for function in Dispatch.get(data.t, [aInvalid])[priority]:
                try:
                    if await function(self, data.d):
                        return
                except BadRequest as ex:
                    log.warn("Bad Request", exc_info=ex)
                except NotFound as ex:
                    log.warn(ex)
                except Insufficient_Permissions as ex:
                    log.info("Insufficient Permissions", exc_info=ex)
                except TypeError as ex:
                    t = traceback.extract_tb(sys.exc_info()[2], limit=-1)
                    if 'missing' in str(ex):
                        error = str(ex).split(' ', 1)[1]
                        err = f'{sys.exc_info()}'
                        print(error)
                        #await self.message(data['d']['channel_id'], error.capitalize())
                    else:
                        print('Error occured:', ex)
                        print(sys.exc_info())
                        print(t)
                except JsonBadRequest as ex:
                    print(ex)
                except Exception as ex:
                    t = traceback.extract_tb(sys.exc_info()[2], limit=-1)
                    log.exception("Dispatch Error %s: %s at %s", type(ex), ex, t, exc_info=ex)
                    log.exception("Location: %s", t[-1])
        return

    async def reconnect(self, data: dict) -> None:
        log.info("Reconnecting %s", self.username)
        await self.resume(data)

    async def invalid_session(self, data: dict) -> None:
        log.info("Invalid Session")
        print(data)
        if data.d:
            log.info("Resuming")
            await self.resume(data)
        else:
            log.info("Reidentifying")
            await self.identify()

    async def hello(self, data: dict) -> None:
        self.heartbeating = asyncio.create_task(self.heartbeat(data.d["heartbeat_interval"]))#, name="Heartbeat")
        await self.identify()

    async def heartbeat_ack(self, data: dict) -> None:
        self.latency = time.perf_counter() - self.heartbeat_sent

    # User
    async def send(self, _json: object):
        raise NotImplementedError

    async def identify(self) -> None:
        log.info("Identifing")
        await self.send(Gateway_Payload(
            op= Gateway_Opcodes.IDENTIFY,
            d= Identify(
                token=self.token,
                properties={
                    "$os": platform.system(),
                    "$browser": "MFramework",
                    "$device": "MFramework"},
                compress=True,
                large_threshold=250,
                guild_subscriptions=self.sub,
                shard=self.shards,
                presence= self.presence,
                intents= self.intents
                )
            )
        )

    async def heartbeat(self, interval: int) -> None:
        self.keepConnection = True
        while self.keepConnection:
            await asyncio.sleep(interval / 1000)
            self.heartbeat_sent = time.perf_counter()
            await self._ws.send_json({"op": 1, "d": self.last_sequence})

    async def resume(self, data: dict) -> None:
        log.info("Resuming, yes?")
        await self.send(Gateway_Payload(
            op = Gateway_Opcodes.RESUME,
            d = Resume(
                token=self.token,
                session_id=self.session_id,
                seq= self.last_sequence
            )
        ))

    async def request_guild_members(self, guild_id: Snowflake, query: str = "", limit: int = 0, presences: bool = False, user_ids: List[Snowflake] = None) -> None:
        await self.send(Gateway_Payload(
            op = Gateway_Opcodes.REQUEST_GUILD_MEMBERS,
            d = Guild_Request_Members(
                guild_id=guild_id,
                query=query,
                limit=limit,
                presences=presences,
                user_ids=user_ids,
                nonce=None
            )
        ))

    async def voice_state_update(self, guild_id: Snowflake, channel_id: Snowflake, mute: bool = False, deaf: bool = True) -> None:
        await self.send(Gateway_Payload(
            op = Gateway_Opcodes.VOICE_STATE_UPDATE,
            d = Gateway_Voice_State_Update(
                guild_id=guild_id,
                channel_id=channel_id,
                self_mute=mute,
                self_deaf=deaf
            )
        ))

    async def presence_update(self, status: Status_Types = "Online", status_name: str = "How the World Burns", status_type: Activity_Types = Activity_Types.WATCHING, afk: bool = False, url: Optional[str] = None) -> None:
        """Status type: 0 - Playing, 1 - Streaming, 2 - Listening, 3 - Watching"""
        await self.send(Gateway_Payload(
            op = Gateway_Opcodes.PRESENCE_UPDATE,
            d = Gateway_Presence_Update(
                since = time.time() if afk else None,
                activities= [Bot_Activity(
                    name=status_name.strip(),
                    type=status_type,
                    url=url)],
                status = status.strip().lower(),
                afk = afk
            )
        ))
    def __init__(self):
        self.opcodes = {i.value: getattr(self, i.name.lower(), aInvalid) for i in Gateway_Opcodes}
