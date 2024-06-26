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

from mdiscord.serializer import from_builtins, to_builtins
from mdiscord.meta_types import NotSerializable

if TYPE_CHECKING:
    from mdiscord.websocket import WebSocket_Client as Bot
else:
    # NOTE: Hack of sorts as otherwise `_decoder` in `Deserializer` throws `NameError`
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
    _Client: NotSerializable[Optional[Bot]] = msgspec.UNSET

    def as_dict(self) -> dict[str, Any]:
        return {
            k: v
            for k, v in msgspec.to_builtins(self, enc_hook=to_builtins).items()
            if get_origin(get_type_hints(self.__class__)[k]) is not NotSerializable
        }

    @classmethod
    def from_dict(cls, **kwargs):
        return msgspec.convert(kwargs, cls, dec_hook=from_builtins)
