# -*- coding: utf-8 -*-
"""
Discord API
----------

Base Types.

:copyright: (c) 2021 Mmesek

"""
from __future__ import annotations

from typing import Optional, TYPE_CHECKING, List, Type, TypeVar
from enum import Flag
from dataclasses import dataclass, is_dataclass, asdict, fields
from datetime import datetime

from mlib.types import Enum
from .serializer import as_dict

if TYPE_CHECKING:
    from .websocket import WebSocket_Client as Bot

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
        return datetime.utcfromtimestamp(ms // 1000.0).replace(microsecond=ms % 1000 * 1000)

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


class Flag(Flag):
    def check(cls, permissions: hex, *values: List[hex]):
        return all([(permissions & permission) == permission for permission in values])

    def current_permissions(cls, permissions: hex):
        current = []
        for permission in cls:
            if (permissions & permission.value) == permission.value:
                current.append(permission.name)
        return current


@dataclass
class DiscordObject:
    _Client: Optional[Bot] = None

    def __post_init__(self):
        for field in self.__dict__:
            if field.startswith("_"):
                continue
            __type = self.__annotations__.get(field) or type(self).__bases__[0].__annotations__.get(field)
            if not __type:
                _annotations = {}
                for i in [i.__annotations__ for i in type(self).mro()[:-2]]:
                    _annotations.update(i)
                __type = _annotations.get(field)
            value = getattr(self, field)
            if value is None or type(value) not in [int, str, bool, type, list, dict]:
                continue
            if type(value) is list and value and is_dataclass(value[0]):
                continue
            _type = __type.replace("List[", "").replace("]", "").replace("Dict[", "")
            if "Dict" in __type:
                k, _type = _type.split(", ")
            is_basic = _type in ["int", "str", "Snowflake", "bool", "datatime"]
            types = {"int": int, "bool": bool, "str": str}
            from . import types as FINAL_TYPES

            _type = types.get(_type, vars(FINAL_TYPES).get(_type))
            # globals().get(_type))
            if _type is None:
                continue
            elif value is list:
                # continue
                self.__setattr__(field, [])
            elif value is dict:
                self.__setattr__(field, {})
            elif "List" in __type:
                try:
                    if issubclass(_type, Enum):
                        self.__setattr__(field, [getattr(_type, i, i) for i in value if i])
                    else:
                        self.__setattr__(
                            field,
                            [
                                _type.from_dict(**i if not is_basic and not is_dataclass(i) else i or None)
                                for i in value or []
                            ],
                        )
                except:
                    try:
                        self.__setattr__(
                            field, [_type.from_dict(**i) if type(i) is not _type else i for i in value or []]
                        )
                    except Exception as ex:
                        self.__setattr__(field, [_type(i) if type(i) is not _type else i for i in value or []])
            elif _type is datetime:
                self.__setattr__(field, _type.fromisoformat(value) if value else _type.now())
            elif "Dict" in __type:
                # k = types.get(k, vars(FINAL_TYPES).get(k))
                try:
                    self.__setattr__(field, {str(_key): _type.from_dict(**_val) for _key, _val in value.items() or {}})
                except Exception as ex:
                    self.__setattr__(field, {str(_key): _val for _key, _val in value.items() or {}})
            else:
                if type(value) is dict:
                    self.__setattr__(field, _type.from_dict(**value if value is not None else value or None))
                elif issubclass(_type, Flag):
                    _flags = []
                    for _flag in _type:
                        if value & _flag.value == 0:
                            _flags.append(_flag)
                    self.__setattr__(field, _flags)
                elif value == 0:
                    self.__setattr__(field, 0 if _type is not str else "0")
                else:
                    self.__setattr__(field, _type(value or (0 if _type is not str else "")))

    # @property
    def as_dict(self):
        _dict = asdict(self)
        for field in _dict:
            if field == "_Client":
                continue
            # if is_dataclass(_dict.get(field)):
            #    _dict[field] = asdict(_dict.get(field))
            else:
                _dict[field] = as_dict(_dict.get(field))
        _dict.pop("_Client")
        return _dict

    @classmethod
    def from_dict(cls, **kwargs):
        return cls(**{k: v for k, v in kwargs.items() if k in list(dir(cls))})
