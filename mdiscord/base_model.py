# -*- coding: utf-8 -*-
"""
Discord API
----------

Base Types.

:copyright: (c) 2021-2024 Mmesek

"""
from typing import Any, Optional, TYPE_CHECKING, Type, TypeVar, get_origin, get_type_hints
from enum import Flag

import msgspec
from mlib.types import Enum

from .serializer import from_builtins, to_builtins
from .meta_types import NotSerializable

if TYPE_CHECKING:
    from .websocket import WebSocket_Client as Bot
else:

    class Bot:
        pass


_T = TypeVar("_T")


class Events(Enum):
    def __call__(self, *args, **kwargs):
        try:
            return self.func.from_dict(*args, **kwargs)
        except AttributeError:
            return kwargs

    def __new__(cls: Type[_T], value: object) -> _T:
        obj = object.__new__(cls)
        obj.func = value
        obj._value_ = len(cls.__members__) + 1
        return obj

    def type(self):
        return self.func


class Flag(Flag):
    def check(cls, permissions: hex, *values: list[hex]):
        return all([(permissions & permission) == permission for permission in values])

    def current_permissions(cls, permissions: hex):
        current = []
        for permission in cls:
            if (permissions & permission.value) == permission.value:
                current.append(permission.name)
        return current


class DiscordObject(msgspec.Struct, kw_only=True, omit_defaults=True):
    _Client: Optional[NotSerializable[Bot]] = msgspec.UNSET

    def as_dict(self):
        from .utils import serializer

        _dict = msgspec.to_builtins(self, enc_hook=serializer)
        for field in _dict:
            if field == "_Client":
                continue
            else:
                _dict[field] = as_dict(_dict.get(field))
        _dict.pop("_Client")
        return _dict

    @classmethod
    def from_dict(cls, **kwargs):
        from .utils import deserializer

        return msgspec.convert(kwargs, cls, dec_hook=deserializer)
