# -*- coding: utf-8 -*-
'''
Utils
----------

Utility functions for internal usage

:copyright: (c) 2021 Mmesek

'''

def dataclass_from_dict(klass, dikt):
    from dataclasses import fields
    try:
        types = {
            "int": int,
            "bool": bool,
            "str": str
        }
        fieldtypes = {}
        for f in fields(klass):
            _type = f.type
            is_list = False
            if 'List' in f.type:
                _type = f.type.replace('List[', '').replace(']', '')
                is_list = True
            _type = types.get(_type, globals().get(_type))
            if is_list:
                fieldtypes[f.name] = (list, _type)
            else:
                fieldtypes[f.name] = _type
        #fieldtypes = {f.name:types.get(f.type, globals().get(f.type)) if 'List' not in f.type else (list, f.type.replace('List[', '').replace(']', '')) for f in fields(klass)}
        #fieldtypes = {f.name:types.get(f.type, globals().get(f.type)) for f in fields(klass)}
        _dict = {}
        for f in dikt:
            if f not in fieldtypes:
                continue
            if type(fieldtypes[f]) is tuple:
                _dict[f] = [dataclass_from_dict(fieldtypes[f][1], i) for i in dikt[f]]
            else:
                _dict[f] = dataclass_from_dict(fieldtypes[f], dikt[f])
        return klass(**_dict)
        #return klass(**{f:dataclass_from_dict(fieldtypes[f],dikt[f]) for f in dikt if f in fieldtypes})
    except Exception as ex:
        #print(ex)
        return dikt

def Permissions(*permissions):
    def inner(f):
        def wrapped(Client, id, *args, **kwargs):
            for permission in permissions:
                if hasattr(Client, 'cache') and id in Client.cache:
                    from .types import Bitwise_Permission_Flags
                    if not Bitwise_Permission_Flags.check(Client.cache[id].permissions, getattr(Bitwise_Permission_Flags, permission)):
                        from .exceptions import Insufficient_Permissions
                        raise Insufficient_Permissions(*permissions)
            return f(Client, id, *args, **kwargs)
        return wrapped #Why was it returning f instead of wrapped before?
    return inner

def count(*intents):
    value = 0
    for intent in intents:
        try:
            from .types import Intents
            value |= getattr(Intents, intent).value
        except AttributeError:
            pass
    return value

import logging
from mlib import logger
log = logging.getLogger("mdiscord")
log.setLevel(logger.log_level)

import asyncio
from typing import Optional, Callable, Dict, List, Tuple
from .base_model import DiscordObject
from .types import Gateway_Events

def default_check(data: DiscordObject) -> bool:
    '''Default check that returns True'''
    return True

class EventListener:
    '''Event Listener mixin'''
    _listeners: Dict[str, List[Tuple[asyncio.Future, Callable[[DiscordObject], bool]]]]
    def wait_for(self, event: str, *, check: Optional[Callable[[DiscordObject], bool]] = default_check, timeout: Optional[float] = None) -> DiscordObject:
        '''Wait for Dispatch event that meets predicate statement

        Params
        ------
        event:
            Dispatch Event to wait for
        check:
            Callable function with predicate to meet
        timeout:
            Timeout after which it should stop waiting for event matching criteria and throw `TimeoutError`
        
        Returns
        -------
        Any:
            Received Event object that matches criteria'''
        if not hasattr(self, '_listeners'):
            self._listeners = {}
        if not (hasattr(Gateway_Events, event.title()) or "direct_message" in event.lower()):
            raise Exception("Event unrecognized")
        event = event.upper()
        if event not in self._listeners:
            self._listeners[event] = []

        future = asyncio.get_event_loop().create_future()
        self._listeners[event].append((future, check))
        return asyncio.wait_for(future, timeout)
    
    def check_listeners(self, event: str, data: DiscordObject) -> bool:
        '''Method checking received data against predicates of current listeners

        Params
        ------
        event:
            Dispatch Event of which listeners should be checked
        data:
            Received Event Payload to check predicates against as well as set result to'''
        if not hasattr(self, '_listeners') or not self._listeners.get(event, None):
            return
        removed = []
        for i, (future, check) in enumerate(self._listeners[event]):
            if future.cancelled():
                removed.append(i)
                continue

            try:
                if check(data):
                    future.set_result(data)
                    removed.append(i)
            except Exception as ex:
                future.set_exception(ex)

        # Inspired by Discord.py, Thanks.
        if len(removed) == len(self._listeners):
            self._listeners.pop(event)
        else:
            for id in reversed(removed):
                del self._listeners[event][id]
        if len(removed):
            return True
