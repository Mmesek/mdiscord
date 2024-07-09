# -*- coding: utf-8 -*-
"""
Discord Opcodes
----------

Discord API Opcodes.

:copyright: (c) 2020 Mmesek
"""

import asyncio, platform
import sys, time, traceback
from collections import Counter
from inspect import getfullargspec
from typing import Callable, Optional, get_args
from datetime import datetime

from mdiscord.exceptions import BadRequest, Insufficient_Permissions, JsonBadRequest, NotFound, SoftError, UserError
from mdiscord.types import (
    Activity_Types,
    Bot_Activity,
    DiscordObject,
    Gateway_Events,
    Gateway_Opcodes,
    Gateway_Payload,
    Gateway_Presence_Update,
    Gateway_Voice_State_Update,
    Identify,
    Identify_Connection_Properties,
    Request_Guild_Members as Guild_Request_Members,
    Resume,
    Snowflake,
    Status_Types,
)
from mdiscord.utils.utils import EventListener, log
from mdiscord.utils.routes import opcode
from collections import defaultdict

DISPATCH: dict[Gateway_Events, dict[int, list[Callable[["Opcodes", DiscordObject], bool]]]] = defaultdict(
    lambda: defaultdict(list)
)
"""Registry containing event names with corresponding lists of target functions to call in order of priority"""
PREDICATES: dict[
    Gateway_Events, dict[Callable[["Opcodes", DiscordObject], bool], list[Callable[[DiscordObject], bool]]]
] = defaultdict(lambda: defaultdict(list))
"""Registry containing event names with corresponding mapping of functions with lists of required predicates"""
INTENTS = 0
"""Required Intents value to execute all registered functions"""


class Opcodes(EventListener):
    counters: Counter = Counter()
    keepConnection: bool = True
    latency: float = 0.0
    heartbeat_sent: float = 0.0
    heartbeating: asyncio.Task
    session_id: str = None
    resume_url: str = None

    async def dispatch(self, data: Gateway_Payload) -> None:
        try:
            data.d = getattr(Gateway_Events, data.t.title())(**data.d)
            data.d._Client = self
        except AttributeError:
            log.debug("Received unknown event type %s", data.t)
            return

        if not getattr(data.d, "guild_id", False) and "MESSAGE" in data.t:
            data.t = "DIRECT_" + data.t
        if getattr(data.d, "is_bot", False):
            data.t = "BOT_" + data.t

        self.counters[data.t] += 1
        if self.check_listeners(data.t, data.d):
            return

        _completed = {}  # Cached result so we don't check same predicate for one payload multiple times
        for priority in sorted(DISPATCH.get(data.t, {})):
            for function in DISPATCH[data.t][priority]:
                try:
                    for predicate in PREDICATES.get(data.t, {}).get(function, []):
                        if not _completed.get(predicate, predicate(data.d)):
                            _completed[predicate] = False
                            break
                    else:
                        if await function(self, data.d):
                            return
                except UserError as ex:
                    log.debug(ex)
                    channel_id = getattr(data.d, "channel_id")
                    if channel_id:
                        await self.create_message(channel_id=channel_id, content=str(ex))
                except JsonBadRequest as ex:
                    log.warn("JSON Bad Request", exc_info=ex)
                except BadRequest as ex:
                    log.warn("Bad Request", exc_info=ex)
                except NotFound as ex:
                    log.warn(ex)
                except Insufficient_Permissions as ex:
                    log.info("Insufficient Permissions", exc_info=ex)
                except TypeError as ex:
                    t = traceback.extract_tb(sys.exc_info()[2], limit=-1)
                    if "missing" in str(ex):
                        error = str(ex).split(" ", 1)[1]
                        err = f"{sys.exc_info()}"
                        log.debug("Missing argument:", exc_info=ex)
                        # await self.message(data['d']['channel_id'], error.capitalize())
                    else:
                        log.warn("Error occured:", exc_info=ex)
                        # print('Error occured:', ex)
                        # print(sys.exc_info())
                        # print(t)
                except SoftError as ex:
                    log.debug(ex)
                except Exception as ex:
                    t = traceback.extract_tb(sys.exc_info()[2], limit=-1)
                    log.exception("Dispatch Error %s: %s at %s", type(ex), ex, t, exc_info=ex)

    async def reconnect(self, data: Gateway_Payload) -> None:
        log.info("Reconnecting %s", self.username)
        await self.resume()

    async def invalid_session(self, data: Gateway_Payload) -> None:
        log.info("Invalid Session")
        if data.d:
            log.info("Resuming after Invalid Session")
            await self.resume()
        else:
            log.info("Reidentifying after Invalid Session")
            await self.identify()

    async def hello(self, data: Gateway_Payload) -> None:
        self.heartbeating = asyncio.create_task(self.heartbeat(data.d["heartbeat_interval"]), name="Heartbeat")
        if self.resume_url and self.session_id:
            await self.resume()
        else:
            await self.identify()

    async def heartbeat_ack(self, data: Gateway_Payload) -> None:
        self.latency = time.perf_counter() - self.heartbeat_sent
        if self.latency > 5:
            log.debug(f"Last heartbeat latency {self.latency}s")

    # User
    async def send(self, _json: object):
        raise NotImplementedError

    @opcode(log="Identifing")
    async def identify(self) -> None:
        return Identify(
            token=self.token,
            properties=Identify_Connection_Properties(os=platform.system(), browser="mdiscord", device="mdiscord"),
            compress=True,
            large_threshold=250,
            shard=self.shards,
            presence=self.presence,
            intents=self.intents,
        )

    async def heartbeat(self, interval: int) -> None:
        self.keepConnection = True
        log.debug(f"Initiated Heartbeat at interval {interval / 1000}s")
        while self.keepConnection:
            await asyncio.sleep(interval / 1000)
            self.heartbeat_sent = time.perf_counter()
            await self._ws.send_json({"op": 1, "d": self.last_sequence})
        log.info("Heartbeat stopped")

    @opcode(log="Resuming")
    async def resume(self) -> None:
        return Resume(token=self.token, session_id=self.session_id, seq=self.last_sequence)

    @opcode(from_args=Guild_Request_Members)
    async def request_guild_members(
        self,
        guild_id: Snowflake,
        query: str = "",
        limit: int = 0,
        presences: bool = False,
        user_ids: list[Snowflake] = None,
    ) -> None: ...

    @opcode(from_args=Gateway_Voice_State_Update)
    async def voice_state_update(
        self, guild_id: Snowflake, channel_id: Snowflake, self_mute: bool = False, self_deaf: bool = False
    ) -> None:
        """
        Example
        -------
        >>> import asyncio
        >>> op = Opcodes()
        >>> asyncio.run(op.voice_state_update(guild_id=1, channel_id=1))
        Gateway_Voice_State_Update(guild_id=1, channel_id=1, self_mute=UNSET, self_deaf=UNSET, _Client=UNSET)
        """

    @opcode
    async def presence_update(
        self,
        status: Status_Types = Status_Types.ONLINE,
        status_name: str = None,
        status_type: Activity_Types = None,
        afk: Optional[datetime] = None,
        url: Optional[str] = None,
    ):
        """
        Example
        -------
        >>> import asyncio
        >>> op = Opcodes()
        >>> asyncio.run(op.presence_update(afk=datetime(2024, 7, 1), status=Status_Types.IDLE))
        Gateway_Presence_Update(since=datetime.datetime(2024, 7, 1, 0, 0), activities=None, status=<Status_Types.IDLE: 'idle'>, afk=True, _Client=UNSET)
        >>> asyncio.run(op.presence_update(status_name=" How the world burns ", status_type=Activity_Types.WATCHING))
        Gateway_Presence_Update(since=None, activities=[Bot_Activity(name='How the world burns', state=UNSET, type=<Activity_Types.WATCHING: 3>, url=None, _Client=UNSET)], status=<Status_Types.ONLINE: 'online'>, afk=False, _Client=UNSET)
        """
        return Gateway_Presence_Update(
            since=afk if isinstance(afk, datetime) else datetime.now() if afk else None,
            activities=[Bot_Activity(status_name.strip(), type=status_type, url=url)] if status_name else None,
            status=status,
            afk=True if afk else False,
        )

    def __init__(self):
        self.opcodes = {i.value: getattr(self, i.name.lower()) for i in Gateway_Opcodes}


def onDispatch(
    f=None,
    priority: int = 100,
    event: str | Gateway_Events = None,
    optional: bool = False,
    predicate: Callable | list[Callable] = None,
):
    """
    Decorator to register function as a listener for Event from Dispatch
    Parameters
    ----------
    f:
        Decorated Function to be registered
    priorty:
        Controls priority in case of multiple functions listening for the same event.
        Function is appended at the end to current functions with same priority
    event:
        Optional Event to which this functions should listen to.
        Default is same as function name
    optional:
        Whether this listener should be excluded from Intent calculation.
        For example, if execution is optional
    predicate:
        Predicate(s) which has to be met in order to call this function

    Example
    -------
    ### Registering listeners
    >>> @onDispatch
    ... async def ready(client, payload): ...
    >>> ready in DISPATCH["READY"][100]
    True

    Function can be renamed if event is specified as either `Gateway_Events`
    >>> @onDispatch(event=Gateway_Events.Message_Create, priority=50)
    ... async def enum_value(a, b): ...
    >>> enum_value in DISPATCH["MESSAGE_CREATE"][50]
    True

    or string
    >>> @onDispatch(event="message_update")
    ... async def string_name(_, d): ...
    >>> string_name in DISPATCH["MESSAGE_UPDATE"][100]
    True

    It's also possible to specify from typehint
    >>> from mdiscord import Message_Delete
    >>> @onDispatch
    ... async def typehint(_, msg: Message_Delete): ...
    >>> typehint in DISPATCH["MESSAGE_DELETE"][100]
    True

    or from argument name
    >>> @onDispatch
    ... async def argument(_, message_delete): ...
    >>> argument in DISPATCH["MESSAGE_DELETE"][100]
    True

    Use union type to register under multiple events at once:
    >>> from mdiscord import Message_Delete_Bulk
    >>> @onDispatch
    ... async def with_union(_, msg: Message_Delete | Message_Delete_Bulk): ...
    >>> with_union in DISPATCH["MESSAGE_DELETE"][100] and with_union in DISPATCH["MESSAGE_DELETE_BULK"][100]
    True

    ### Event filtering

    Filter events using custom predicate:
    >>> predicate = lambda x: x.guild_id == 1
    >>> @onDispatch(predicate=predicate)
    ... async def message_create(_, msg): ...
    >>> predicate in PREDICATES["MESSAGE_CREATE"][message_create]
    True

    Or multiple:
    >>> predicate_a = lambda x: x.guild_id == 1
    >>> predicate_b = lambda x: x.message_id == 1
    >>> @onDispatch(predicate=[predicate_a, predicate_b])
    ... async def message_update(_, msg): ...
    >>> all(p in PREDICATES["MESSAGE_UPDATE"][message_update] for p in [predicate_a, predicate_b])
    True
    """

    def inner(f):
        # Set name from event or function's name
        names: set[str] = {event or f.__name__}

        if any(clean_name(name) not in Gateway_Events._member_names_ for name in names):
            # If name is still not proper try to guess from typehint
            args = getfullargspec(f)
            k = args.args[1]  # Second parameter is always data
            if v := args.annotations.get(k, None):
                # If we are dealing with union, add both
                names.update({i.__name__ for i in get_args(v) or [v]})
            names.add(k)

        for name in names:
            if type(name) is str and clean_name(name) not in Gateway_Events._member_names_:
                # Make sure we only add valid events
                continue
            _name = Gateway_Events.by_str(clean_name(name))

            if not optional:
                global INTENTS
                INTENTS |= _name.annotation(0)

            name = _name.upper()
            if predicate:
                PREDICATES[name][f] += predicate if type(predicate) is list else [predicate]

            DISPATCH[name][priority].append(f)

        return f

    if f:
        return inner(f)
    return inner


def clean_name(name: str) -> str:
    """
    Example
    -------
    >>> clean_name("DIRECT_BOT_MESSAGE")
    'Message'
    """
    return name.upper().replace("DIRECT_", "").replace("BOT_", "").title()
