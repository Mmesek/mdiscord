# -*- coding: utf-8 -*-
"""
Route Decorator
----------

Helper decorator to automate creating API interface

:copyright: (c) 2024 Mmesek
"""

import inspect
import re
from typing import get_args, get_origin, get_type_hints
from functools import wraps

from mdiscord.types import DiscordObject, Gateway_Opcodes, Gateway_Payload
from mdiscord.utils.utils import log as _log

PATH_PARAM = re.compile(r"/\{(.*?)\}")
MAJOR_PARAMS = ["application_id", "guild_id", "channel_id", "webhook_id", "webhook_token"]


def route(method: str, path: str, json_as_form_data: bool = False):
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
        type_hints = get_type_hints(f)
        module = inspect.getmodule(f).__name__
        args = inspect.getfullargspec(f)

        PATH = PATH_PARAM.findall(path)
        ARGUMENTS = [k for k in type_hints.keys() if k != "return"]
        QUERY = set(args.kwonlyargs)  # Retrieve ALL query params from func definition (keyword-only parameters)
        JSON = {
            a for a in args.args if a not in PATH and a not in {"self"}
        }  # Retrieve ALL json params from func definition (Positionla parameters)

        RESULT = type_hints.get("return", None)
        result_args = get_args(RESULT)
        origin = get_origin(RESULT)

        if result_args:
            RESULT = result_args[0]

        IS_LIST = origin is list
        IS_METHOD = module.split(".")[-1] != "endpoints"  # TODO: Set if route is attached to an object, not bot though

        async def _api_call(self, *args, payload=None, reason: str = None, **kwargs):
            def create_object(result):
                if issubclass(RESULT, DiscordObject):
                    result = RESULT.from_dict(**result)
                    result._Client = self
                return result

            # Overwrite actual call here
            if IS_METHOD:
                kwargs.update()  # TODO: Set path params from available attributes here
                # NOTE: this is to be taken from context we have, which means object we operate on if the request originates from `Model.endpoint()``
            kwargs.update(zip(ARGUMENTS, args))

            try:
                _path = path.format(**{k: v for k, v in kwargs.items() if k in PATH})
            except KeyError as ex:
                _log.debug("Path parameter %s is not a part of MAJOR_PARAMS", ex)

            r = await self.api_call(
                path=_path,
                method=method,
                reason=reason,
                params={k: v for k, v in kwargs.items() if k in QUERY},
                json={k: v for k, v in kwargs.items() if k in JSON},
                payload=payload,
                # bucket="|".join([str(kwargs.get(major, "-")) for major in MAJOR_PARAMS]), # NOTE: String might be bigger in size than a tuple
                bucket=tuple(kwargs.get(major, None) for major in MAJOR_PARAMS),
            )

            if IS_LIST:
                items = []
                for i in r:
                    r = create_object(i)
                    items.append(r)
                r = items
            else:
                r = create_object(r)

            return r

        return _api_call

    return init


def opcode(cls=None, *, from_args: DiscordObject = None, log: str = None):
    def init(f):
        OPCODE = Gateway_Opcodes.by_str(f.__name__.upper())

        @wraps(f)
        async def _send(self, *args, **kwargs):
            if log:
                _log.debug(log.format(self))

            if from_args:
                data = from_args(*args, **kwargs)
            else:
                data = await f(self, *args, **kwargs)
            await self.send(Gateway_Payload(op=OPCODE, d=data))
            return data

        return _send

    if cls:
        return init(cls)
    return init
