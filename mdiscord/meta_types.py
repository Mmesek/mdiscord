# -*- coding: utf-8 -*-
"""
Metadata Types
----------

Metadata types used for conversions to allow more convenient usage.

:copyright: (c) 2024 Mmesek
"""

from datetime import datetime, timedelta, UTC
from typing import Generic, TypeVar

T = TypeVar("T")

DISCORD_EPOCH = 1420070400000
BASE_URL = "https://discord.com/"
CDN_URL = "https://cdn.discordapp.com/"


class NotSerializable(Generic[T]):
    pass


class Nullable(Generic[T]):
    pass


class UnixTimestamp(datetime):
    pass


class Duration(timedelta):
    pass


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
