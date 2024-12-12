# -*- coding: utf-8 -*-
"""
Metadata Types
----------

Metadata types used for conversions to allow more convenient usage.

:copyright: (c) 2024 Mmesek
"""

from datetime import datetime, timedelta, UTC
from typing import TypeVar, Type, Annotated
from enum import IntFlag
from mlib.types import Enum

T = TypeVar("T")

DISCORD_EPOCH = 1420070400000
BASE_URL = "https://discord.com/"
CDN_URL = "https://cdn.discordapp.com/"

Nullable = Annotated[T | None, "nullable"]
NotSerializable = Annotated[T, "not_serializable"]


class UnixTimestamp(datetime):
    """Helper type to support converting `Unix Timestamps` to `Datetime` objects and vice-versa"""


class Duration(timedelta):
    """Helper type to support converting integers representing seconds to `timedelta` and vice-versa"""


class Enum(Enum):
    def upper(self):
        return self.name.upper()

    def title(self):
        return self.name.title()

    def annotation(cls, default=None):
        return cls.__annotations__.get(cls.name, default)

    @classmethod
    def by_str(cls: Type[T], name: str) -> Type[T]:
        return getattr(cls, name)

    @classmethod
    def _missing_(cls, value):
        """
        >>> class MyEnum(NotStrictEnum):
        ...     a = "1"
        >>> MyEnum("2")
        <MyEnum.a: '1'>
        """
        return [v for v in cls][0]


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


NotStrictEnum = Enum


class Flag(IntFlag):
    def check(cls, permissions: hex, *values: list[hex]):
        """
        Example
        -------
        >>> class MyFlag(Flag):
        ...     A = 1
        ...     B = 2
        ...     C = 3
        ...     D = 4
        >>> MyFlag.A.check(2, 2)
        True
        >>> MyFlag.A.check(4, 2)
        False
        """
        return all([(permissions & permission) == permission for permission in values])

    def current_permissions(cls, permissions: hex):
        """
        Example
        -------
        >>> class MyFlag(Flag):
        ...     A = 1
        ...     B = 2
        ...     C = 3
        ...     D = 4
        >>> MyFlag.current_permissions(MyFlag, 2)
        ['B']
        >>> MyFlag.current_permissions(MyFlag, 8)
        []
        >>> MyFlag.current_permissions(MyFlag, 5)
        ['A', 'D']
        """
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

    @property
    def timestamp(self):
        """
        Example
        -------
        >>> Snowflake(517445947446525952).timestamp
        1543439127552
        """
        return (self._value >> 22) + DISCORD_EPOCH

    @property
    def internal_worker_id(self):
        """
        Example
        -------
        >>> Snowflake(517445947446525952).internal_worker_id
        2
        """
        return (self._value & 0x3E0000) >> 17

    @property
    def internal_process_id(self):
        """
        Example
        -------
        >>> Snowflake(517445947446525952).internal_process_id
        0
        """
        return (self._value & 0x1F000) >> 12

    @property
    def increment(self):
        """
        Example
        -------
        >>> Snowflake(517445947446525952).increment
        0
        """
        return self._value & 0xFFF

    @property
    def as_datetime(self):
        """
        Example
        -------
        >>> Snowflake(517445947446525952).as_datetime
        datetime.datetime(2018, 11, 28, 21, 5, 27, 552000, tzinfo=datetime.timezone.utc)
        """
        ms = self.timestamp
        return datetime.fromtimestamp(ms // 1000.0, UTC).replace(microsecond=ms % 1000 * 1000)

    as_date = as_datetime

    def styled_date(self, style: str = "f") -> str:
        """
        Example
        -------
        >>> Snowflake(517445947446525952).styled_date()
        '<t:1543439127:f>'
        """
        return f"<t:{int(self.timestamp / 1000.0)}{':' + style if style else ''}>"
