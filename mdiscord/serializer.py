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
    from enum import Flag
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
        if object._Client:
            object._Client = None
        return object.as_dict()
    elif isinstance(object, datetime):
        return object.isoformat()
    elif isinstance(object, Enum) or isinstance(object, Flag):
        return object.value
    elif type(object) is type:
        return None
    return object

class Serializer:
    token: str = None
    _auth_type: str = "Bot"
    def _prepare_payload(self, **kwargs):
        if 'headers' not in kwargs:
            kwargs['headers'] = []
        if self.token:
            kwargs['headers'].append(("Authorization", f"{self._auth_type} {self.token}"))
        if kwargs.get('reason'):
            kwargs['headers'].append(("X-Audit-Log-Reason", kwargs.pop('reason')))
        if not kwargs.get('file'):
            kwargs['headers'].append(("Content-Type", "application/json"))
        else:
            import aiohttp
            kwargs['data'] = aiohttp.FormData()
            import ujson as json
            kwargs['data'].add_field("payload_json", json.dumps(as_dict(kwargs["json"])))
            kwargs['data'].add_field("file", kwargs["file"],
                filename=kwargs["filename"],
                content_type="application/octet-stream"
            )
            kwargs.pop('json')

        kwargs = self._serialize(**kwargs)
        return kwargs

    def _serialize(self, **kwargs):
        from mlib.utils import remove_None
        if kwargs.get('json'):
            kwargs['json'] = as_dict(kwargs['json'])
            kwargs['json'] = remove_None(kwargs.get('json',{}))
            if type(kwargs['json']) is dict:
                for key, value in kwargs['json'].items():
                    if key in {'embeds', 'components'} and type(value) is not list:
                        kwargs['json'][key] = [value]
        if kwargs.get('params'):
            kwargs["params"] = remove_None(kwargs.get("params"))
            for param in kwargs["params"]:
                kwargs["params"][param] = str(kwargs["params"][param])
            for i in ["before", "after", "between"]:
                if kwargs["params"].get(i, False) is None:
                    kwargs.pop(i)
        kwargs.pop('filename', None)
        kwargs.pop('file', None)
        kwargs = remove_None(kwargs)
        return kwargs