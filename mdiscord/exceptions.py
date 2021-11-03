# -*- coding: utf-8 -*-
'''
Discord Exceptions
----------

Discord Exceptions.

:copyright: (c) 2021 Mmesek

'''
from typing import Dict, Any, Tuple

def find_error(obj: Dict[str, Any], errors: Dict[str, Any], previous: Dict[str, Any] = None) -> Tuple[Dict, Dict]:
    for error in errors:
        if error.isdigit():
            try:
                return find_error(obj[int(error)], errors[error], obj)
            except:
                return previous, errors[error]
        try:
            return find_error(obj.get(error), errors[error], obj)
        except:
            return previous, errors[error]
    return None, None

class DiscordError(Exception):
    '''Base Discord Error'''
    pass

class Insufficient_Permissions(DiscordError):
    '''User doesn't have enough permissions'''
    pass

class HTTP_Error(DiscordError):
    '''Basic Error that occured during HTTP connection'''
    def __init__(self, reason: str, method: str, path: str, extra: str = None) -> None:
        self.reason = reason
        self.method = method
        self.path = path
        super().__init__(f"[{self.method}] {self.path} | [{self.reason}]{extra or ''}")

class RequestError(HTTP_Error):
    '''Error that occured while sending request to Discord'''
    pass

class BadRequest(RequestError):
    '''Error caused by malformated request'''
    def __init__(self, reason: str, msg: str, method: str, path: str, *args: object, payload: Dict[str, Any] = None, errors: Dict[str, Any] = None) -> None:
        self.msg = msg
        payload, errors = find_error(payload, errors)
        import ujson
        if isinstance(payload, dict):
            payload = ujson.dumps(payload, indent=2)
        try:
            errors = ujson.dumps(errors, indent=2)
        except:
            pass
        super().__init__(reason, method, path, f" {self.msg}\nPayload: {payload}\nError: {errors}")

class NotFound(RequestError):
    '''Error caused by 404 response from Discord'''
    pass

class JsonBadRequest(BadRequest):
    '''Error caused by malformated request with JSON response'''
    pass

class SoftError(Exception):
    '''Non fatal exception to be raised by user code that is not important enough to log'''
    pass