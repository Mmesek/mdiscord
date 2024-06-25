# -*- coding: utf-8 -*-
"""
Discord API
----------

Base Types.

:copyright: (c) 2021-2024 Mmesek

"""
from typing import Optional, TYPE_CHECKING, Type, TypeVar
from enum import Flag
from datetime import datetime, UTC
import msgspec

from mlib.types import Enum
from .serializer import as_dict
from .meta_types import NotSerializable

if TYPE_CHECKING:
    from .websocket import WebSocket_Client as Bot
else:

    class Bot:
        pass


_T = TypeVar("_T")


DISCORD_EPOCH = 1420070400000
BASE_URL = "https://discord.com/"
CDN_URL = "https://cdn.discordapp.com/"


class Snowflake(int):
    """Base ID Type for Discord objects"""

    _value: int = 0

    def __new__(cls, value=0):
        return super(Snowflake, cls).__new__(cls, value)

    def __init__(self, value=0):
        self._value = int(value)

    #    def __class_getitem__(cls, key='value'):
    #        return cls._value
    @property
    def timestamp(self):
        return (self._value >> 22) + DISCORD_EPOCH

    @property
    def internal_worker_id(self):
        return (self._value & 0x3E0000) >> 17

    @property
    def internal_process_id(self):
        return (self._value & 0x1F000) >> 12

    @property
    def increment(self):
        return self._value & 0xFFF

    @property
    def as_date(self):
        ms = (self._value >> 22) + DISCORD_EPOCH
        return datetime.fromtimestamp(ms // 1000.0, UTC).replace(microsecond=ms % 1000 * 1000)

    def styled_date(self, style: str = None) -> str:
        return f"<t:{int(self.timestamp/1000.0)}{':'+style if style else ''}>"


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
