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
