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

from mdiscord.types import DiscordObject
from mdiscord.utils.utils import log

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
        # Init here
        type_hints = get_type_hints(f)
        module = inspect.getmodule(f).__name__
        args = inspect.getfullargspec(f)

        PATH = PATH_PARAM.findall(path)
        ARGUMENTS = [
            k for k in type_hints.keys() if k != "return"
        ]  # NOTE: Don't include path params (named args in function below)
        QUERY = set(args.kwonlyargs)  # TODO: Retrieve ALL query params from func definition (keyword-only arguments)
        JSON = {
            a for a in args.args if a not in PATH and a not in {"self"}
        }  # TODO: Retrieve ALL json params from func definition ("Regular" params)

        RESULT = type_hints.get("return", None)
        result_args = get_args(RESULT)
        origin = get_origin(RESULT)

        if result_args:
            RESULT = result_args[0]

        IS_LIST = origin is list
        IS_METHOD = (
            module.split(".")[-1] != "endpoints"
        )  # False  # TODO: Set if route is attached to an object, not bot though

        async def _api_call(self, *args, reason: str = None, **kwargs):
            def create_object(result):
                if issubclass(RESULT, DiscordObject):
                    result = RESULT.from_dict(**result)
                    result._Client = self
                return result

            # Overwrite actual call here
            if IS_METHOD:
                kwargs.update()  # TODO: Set path params from available attributes here
            kwargs.update(zip(ARGUMENTS, args))

            try:
                _path = path.format(**{k: v for k, v in kwargs.items() if k in PATH})
            except KeyError as ex:
                log.debug("Path parameter %s is not a part of MAJOR_PARAMS", ex)

            r = await self.api_call(
                path=_path,
                method=method,
                reason=reason,
                params={k: v for k, v in kwargs.items() if k in QUERY},
                json={k: v for k, v in kwargs.items() if k in JSON},
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
