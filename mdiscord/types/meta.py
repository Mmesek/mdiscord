# -*- coding: utf-8 -*-
"""
Metadata Types
----------

Metadata types used for conversions to allow more convenient usage.

:copyright: (c) 2024 Mmesek
"""

from datetime import UTC, datetime, timedelta
from enum import Enum, Flag
from typing import Generic, Type, TypeVar

T = TypeVar("T")

DISCORD_EPOCH = 1420070400000
BASE_URL = "https://discord.com/"
CDN_URL = "https://cdn.discordapp.com/"

Nullable = T | None


class NotSerializable(Generic[T]):
    pass


class UnixTimestamp(datetime):
    pass


class Duration(timedelta):
    pass


class Events(Enum):
    def __call__(self, *args, **kwargs):
        try:
            return self.func.from_dict(*args, **kwargs)
        except AttributeError:
            return kwargs

    def __new__(cls: Type[T], value: object) -> T:
        obj = object.__new__(cls)
        obj.func = value
        obj._value_ = len(cls.__members__) + 1
        return obj

    def type(self):
        return self.func


class NotStrictEnum(Enum):
    @classmethod
    def _missing_(cls, value):
        # NOTE: VERY temporary #HACK
        return [v for v in cls][0]


class Flag(Flag):
    def check(cls, permissions: hex, *values: list[hex]):
        return all([(permissions & permission) == permission for permission in values])

    def current_permissions(cls, permissions: hex):
        current = []
        for permission in cls:
            if (permissions & permission.value) == permission.value:
                current.append(permission.name)
        return current


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
        return f"<t:{int(self.timestamp / 1000.0)}{':' + style if style else ''}>"
