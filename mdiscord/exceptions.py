# -*- coding: utf-8 -*-
"""
Discord Exceptions
----------

Discord Exceptions.

:copyright: (c) 2021 Mmesek
"""

from typing import Any
import json


def find_error(obj: dict[str, Any], errors: dict[str, Any], previous: dict[str, Any] = None) -> tuple[dict, dict]:
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
    """Base Discord Error"""


class Insufficient_Permissions(DiscordError):
    """User doesn't have enough permissions"""


class HTTP_Error(DiscordError):
    """Basic Error that occured during HTTP connection"""

    def __init__(self, reason: str, method: str, path: str, extra: str = None) -> None:
        self.reason = reason
        self.method = method
        self.path = path
        super().__init__(f"[{self.method}] {self.path} | [{self.reason}]{extra or ''}")


class RequestError(HTTP_Error):
    """Error that occured while sending request to Discord"""


class BadRequest(RequestError):
    """Error caused by malformated request"""

    def __init__(
        self,
        reason: str,
        msg: str,
        method: str,
        path: str,
        *args: object,
        payload: dict[str, Any] = None,
        errors: dict[str, Any] = None,
    ) -> None:
        self.msg = msg
        payload, errors = find_error(payload, errors)
        if isinstance(payload, dict):
            payload = json.dumps(payload, indent=2)
        try:
            errors = json.dumps(errors, indent=2)
        except:
            pass
        super().__init__(reason, method, path, f" {self.msg}\nPayload: {payload}\nError: {errors}")


class NotFound(RequestError):
    """Error caused by 404 response from Discord"""


class JsonBadRequest(BadRequest):
    """Error caused by malformated request with JSON response"""


class SoftError(Exception):
    """Non fatal exception to be raised by user code that is not important enough to log"""


class UserError(SoftError):
    """Error caused by user input. To be returned to user"""
