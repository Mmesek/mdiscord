# -*- coding: utf-8 -*-
'''
Discord Exceptions
----------

Discord Exceptions.

:copyright: (c) 2021 Mmesek

'''
from typing import Dict, Any


class Insufficient_Permissions(Exception):
    pass

class RequestError(Exception):
    pass

class BadRequest(RequestError):
    def __init__(self, reason: str, msg: str, method: str, path: str, *args: object, payload: Dict[str, Any] = None) -> None:
        self.reason = reason
        self.msg = msg
        self.method = method
        self.path = path
        self.payload = payload
        if isinstance(payload, dict):
            import ujson
            payload = ujson.dumps(payload, indent=2)
        super().__init__(f"[{self.method}] {self.path} | [{self.reason}] {self.msg}\nPayload: {payload}")

class NotFound(RequestError):
    pass

class JsonBadRequest(BadRequest):
    pass
