# -*- coding: utf-8 -*-
'''
Serialization JSON<->Types
----------

Serializer & Deserializer

:copyright: (c) 2021 Mmesek

'''

class Deserializer:
    def __init__(self):
        import zlib
        self._buffer = bytearray()
        self._zlib = zlib.decompressobj()
    def __call__(self, msg: bytes):
        import ujson as json
        if type(msg) is bytes:
            self._buffer.extend(msg)
            if len(msg) >= 4:
                if msg[-4:] == b'\x00\x00\xff\xff':
                    msg = self._zlib.decompress(self._buffer).decode('utf-8')
                    self._buffer = bytearray()
                else:
                    return
            else:
                return
        from .types import Gateway_Payload
        return Gateway_Payload(**json.loads(msg))

def as_dict(object):
    from datetime import datetime
    from dataclasses import is_dataclass
    from . import Enum
    if type(object) is dict:
        _object = {}
        for key in object:
            if key not in ['_Client', 'total_characters']:
                if object[key] is None:
                    continue
                _object[key] = as_dict(object[key])
        return _object
    elif type(object) is list:
        return [as_dict(key) for key in object]
    elif is_dataclass(object):
        return object.as_dict()
    elif isinstance(object, datetime):
        return object.isoformat()
    elif isinstance(object, Enum):
        return object.value
    elif type(object) is type:
        return None
    return object