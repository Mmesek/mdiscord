# -*- coding: utf-8 -*-
"""
Utils
-----

Utility functions for internal usage

:copyright: (c) 2021 Mmesek
"""

import asyncio
import logging
from typing import Callable, Optional, Tuple, Union

from mlib import logger

from mdiscord.exceptions import Insufficient_Permissions
from mdiscord.types import Bitwise_Permission_Flags, DiscordObject, Gateway_Events, Intents

log = logging.getLogger("mdiscord")
log.setLevel(logger.log_level)


def Permissions(*permissions):
    def inner(f):
        def wrapped(Client, id, *args, **kwargs):
            for permission in permissions:
                if hasattr(Client, "cache") and id in Client.cache:
                    if not Bitwise_Permission_Flags.check(
                        Client.cache[id].permissions, getattr(Bitwise_Permission_Flags, permission)
                    ):
                        raise Insufficient_Permissions(*permissions)
            return f(Client, id, *args, **kwargs)

        return f  # wrapped

    return inner


def count(*intents):
    """
    Example
    -------
    >>> count("GUILDS", "GUILD_MEMBERS", "Unknown")
    3
    """
    value = 0
    for intent in intents:
        try:
            value |= getattr(Intents, intent).value
        except AttributeError:
            pass
    return value


class EventListener:
    """Event Listener mixin"""

    _listeners: dict[str, list[Tuple[asyncio.Future, Callable[[DiscordObject], bool]]]]

    def wait_for(
        self,
        event: Union[str, Gateway_Events],
        repeat: int = 1,
        *,
        check: Optional[Callable[[DiscordObject], bool]],
        timeout: Optional[float] = None,
    ) -> DiscordObject:
        """Wait for Dispatch event that meets predicate statement

        Parameters
        ----------
        event:
            Dispatch Event to wait for
        repeat:
            How many times this event should be waited for
        check:
            Callable function with predicate to meet
        timeout:
            Timeout after which it should stop waiting for event matching criteria and throw `TimeoutError`

        Returns
        -------
        Any:
            Received Event object that matches criteria"""
        if not hasattr(self, "_listeners"):
            self._listeners = {}
        if type(event) is Gateway_Events:
            event = event.name
        elif not (hasattr(Gateway_Events, event.title()) or "direct_message" in event.lower()):
            raise Exception("Event unrecognized")
        event = event.upper()
        if event not in self._listeners:
            self._listeners[event] = []

        future = asyncio.get_event_loop().create_future()
        for i in range(repeat):
            self._listeners[event].append((future, check))
        return asyncio.wait_for(future, timeout)

    def check_listeners(self, event: str, data: DiscordObject) -> bool:
        """Method checking received data against predicates of current listeners

        Parameters
        ----------
        event:
            Dispatch Event of which listeners should be checked
        data:
            Received Event Payload to check predicates against as well as set result to"""
        if not hasattr(self, "_listeners") or not self._listeners.get(event, None):
            return
        removed = []
        predicates_met = []
        for i, (future, check) in enumerate(self._listeners[event]):
            if future.cancelled():
                removed.append(i)
                continue
            if check in predicates_met:
                continue

            try:
                if check(data):
                    future.set_result(data)
                    predicates_met.append(check)
                    removed.append(i)
            except Exception as ex:
                try:
                    future.set_exception(ex)
                except asyncio.InvalidStateError:
                    log.exception(
                        "InvalidStateError was raised by future waiting for event %s with data %s", event, data
                    )
                    removed.append(i)

        # Inspired by Discord.py, Thanks.
        if len(removed) == len(self._listeners[event]):
            self._listeners.pop(event)
        else:
            for id in reversed(removed):
                del self._listeners[event][id]
        if len(removed):
            return True
