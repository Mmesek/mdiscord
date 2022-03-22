# -*- coding: utf-8 -*-
'''
Discord API
----------

Discord API.

:copyright: (c) 2020 Mmesek

'''
from typing import Union

from .types import * # noqa: F401
from .websocket import WebSocket_Client as Client # noqa: F401
from .exceptions import * # noqa: F401

def onDispatch(f=None, priority: int=100, event: Union[str, Gateway_Events]=None, optional: bool = False):
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
    """
    def inner(f):
        from .opcodes import Dispatch
        name = f.__name__.upper()
        if event:
            if type(event) is Gateway_Events:
                name = event.name
            name = event.upper()
        if optional:
            f._optional = optional
        if name not in Dispatch:
            Dispatch[name] = {}
        if priority not in Dispatch[name]:
            Dispatch[name][priority] = []
        Dispatch[name][priority].append(f)
        return f
    if f:
        return inner(f)
    return inner

@onDispatch
async def ready(self: Client, ready: Ready):
    self.user_id = ready.user.id
    self.username = ready.user.username
    from .utils import log
    log.info("Connected as %s", ready.user.username)
