# -*- coding: utf-8 -*-
'''
Discord Exceptions
----------

Discord Exceptions.

:copyright: (c) 2021 Mmesek

'''
from typing import Dict, Any

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
    def __init__(self, reason: str, msg: str, method: str, path: str, *args: object, payload: Dict[str, Any] = None) -> None:
        self.msg = msg
        self.payload = payload
        if isinstance(payload, dict):
            import ujson
            payload = ujson.dumps(payload, indent=2)
        super().__init__(reason, method, path, f"{self.msg}\nPayload: {payload}")

class NotFound(RequestError):
    '''Error caused by 404 response from Discord'''
    pass

class JsonBadRequest(BadRequest):
    '''Error caused by malformated request with JSON response'''
    pass
