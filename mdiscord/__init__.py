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

def onDispatch(f):
    def inner(f):
        from .opcodes import Dispatch
        if f.__name__.upper() not in Dispatch:
            Dispatch[f.__name__.upper()] = []
        Dispatch[f.__name__.upper()].append(f)
        return f
    return inner(f)
