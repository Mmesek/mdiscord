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


import re

PATH_PARAM = re.compile(r"/\{(.*)\}")
MAJOR_PARAMS = ["guild_id", "channel_id", "webhook_id", "webhook_token"]


def route(method: str, path: str):
    """
    Route decorator, creates an endpoint call based on parameters.

    Regular parameters are interpreted as JSON body arguments unless they are present in `path`.
    Keyword-only parameters are interpreted as Query arguments (?k=v&k2=v2).

    Return type is used for autocasting. Supports casting to an array.

    Parameters
    ----------
    method: `str`
        HTTP Method used when sending Request.
    path: `str`
        Path to which send Request. Supports `/{path}/` params.

    Returns
    -------
    `Any`, depends on decorated function.
    """

    def init(f):
        # Init here
        PATH = PATH_PARAM.findall(path)
        ARGUMENTS = []  # NOTE: Don't include path params (named args in function below)
        QUERY = {}  # TODO: Retrieve ALL query params from func definition (keyword-only arguments)
        JSON = {}  # TODO: Retrieve ALL json params from func definition ("Regular" params)
        IS_LIST = False  # TODO: Check if return type is a list
        RESULT = f  # TODO: Retrieve from function definition
        IS_METHOD = False  # TODO: Set if route is attached to an object, not bot though

        async def _api_call(self, reason: str = None, *args, **kwargs):
            # Overwrite actual call here
            if IS_METHOD:
                kwargs.update()  # TODO: Set path params from available attributes here
            kwargs.update(zip(ARGUMENTS, args))
            r = await self.api_call(
                path=path.format(**{k: v for k, v in kwargs.items() if k in PATH}),
                method=method,
                reason=reason,
                params={k: v for k, v in kwargs.items() if k in QUERY},
                json={k: v for k, v in kwargs.items() if k in JSON},
                # bucket="|".join([str(kwargs.get(major, "-")) for major in MAJOR_PARAMS]), # NOTE: String might be bigger in size than a tuple
                bucket=(kwargs.get(major, None) for major in MAJOR_PARAMS),
            )
            return [RESULT(i) for i in r] if IS_LIST else RESULT(r)

        return _api_call

    return init
