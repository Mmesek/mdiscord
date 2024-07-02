import re
import inspect
from typing import get_type_hints, get_origin, get_args
from mdiscord.base_model import DiscordObject
from mdiscord.utils import log

PATH_PARAM = re.compile(r"/\{(.*?)\}")
MAJOR_PARAMS = ["guild_id", "channel_id", "webhook_id", "webhook_token"]


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
        origin = get_origin(type_hints.get("return", None))
        args = inspect.getfullargspec(f)

        PATH = PATH_PARAM.findall(path)
        ARGUMENTS = [
            k for k in type_hints.keys() if k != "return"
        ]  # NOTE: Don't include path params (named args in function below)
        QUERY = set(args.kwonlyargs)  # TODO: Retrieve ALL query params from func definition (keyword-only arguments)
        JSON = {
            a for a in args.args if a not in PATH and a not in {"self"}
        }  # TODO: Retrieve ALL json params from func definition ("Regular" params)
        IS_LIST = origin is list  # TODO: Check if return type is a list
        RESULT = type_hints.get("return", None)  # TODO: Retrieve from function definition
        IS_METHOD = (
            module.split(".")[-1] != "endpoints"
        )  # False  # TODO: Set if route is attached to an object, not bot though

        async def _api_call(self, *args, reason: str = None, **kwargs):
            # Overwrite actual call here
            if IS_METHOD:
                kwargs.update()  # TODO: Set path params from available attributes here
            kwargs.update(zip(ARGUMENTS, args))

            try:
                _path = path.format(**{k: v for k, v in kwargs.items() if k in PATH})
            except:
                # NOTE: testing only
                breakpoint

            r = await self.api_call(
                path=_path,
                method=method,
                reason=reason,
                params={k: v for k, v in kwargs.items() if k in QUERY},
                json={k: v for k, v in kwargs.items() if k in JSON},
                # bucket="|".join([str(kwargs.get(major, "-")) for major in MAJOR_PARAMS]), # NOTE: String might be bigger in size than a tuple
                bucket=tuple(kwargs.get(major, None) for major in MAJOR_PARAMS),
            )

            arg = get_args(RESULT)

            if not issubclass(arg[0] if arg else RESULT, DiscordObject):
                return r

            if IS_LIST:
                items = []
                for i in r:
                    # BUG: Result is not always a type!
                    # NOTE: Check against union types too!
                    r = RESULT.from_dict(**i)
                    r._Client = self
                    items.append(r)
                return items

            if type(r) is list:
                log.warn(
                    "Expected result is either wrong or Discord sends Union of List and Single element which we need to handle!"
                )

            r = RESULT.from_dict(**r)
            r._Client = self

            return r

        return _api_call

    return init
