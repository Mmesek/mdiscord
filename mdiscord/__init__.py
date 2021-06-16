# -*- coding: utf-8 -*-
'''
Discord API
----------

Discord API.

:copyright: (c) 2020 Mmesek

'''
from .types import * # noqa: F401
from .client import WebSocket_Client as Client # noqa: F401
from .exceptions import * # noqa: F401

def onDispatch(f=None, priority=100, event=None):
    def inner(f):
        from .opcodes import Dispatch
        name = f.__name__.upper()
        if event:
            name = event.upper()
        if name not in Dispatch:
            Dispatch[name] = {}
        if priority not in Dispatch[name]:
            Dispatch[name][priority] = []
        Dispatch[name][priority].append(f)
        return f
    if f:
        return inner(f)
    return inner
