# -*- coding: utf-8 -*-
"""
Serialization JSON<->Types
----------

Serializer & Deserializer

:copyright: (c) 2021 Mmesek

"""
import aiohttp
import zlib
import msgspec
from datetime import UTC
from typing import Any

from .meta_types import Snowflake, UnixTimestamp, Duration


def to_builtins(x: Any):
    if isinstance(x, Snowflake):
        return x._value
    elif isinstance(x, UnixTimestamp):
        return x.timestamp() * 1000
    elif isinstance(x, Duration):
        return int(x.total_seconds())
    return None


def from_builtins(typ: type, x: Any):
    if typ is Snowflake:
        return Snowflake(x)
    elif typ is UnixTimestamp:
        return UnixTimestamp.fromtimestamp(x / 1000, UTC)
    elif typ is Duration:
        return Duration(seconds=x)
    return x


ENCODER = msgspec.json.Encoder(enc_hook=to_builtins)


class Deserializer:
    def __init__(self):
        self._buffer = bytearray()
        self._zlib = zlib.decompressobj()
        from .types import Gateway_Payload

        self._decoder = msgspec.json.Decoder(Gateway_Payload, dec_hook=from_builtins)

    def __call__(self, msg: bytes):
        if type(msg) is bytes:
            self._buffer.extend(msg)
            if len(msg) >= 4:
                if msg[-4:] == b"\x00\x00\xff\xff":
                    msg = self._zlib.decompress(self._buffer).decode("utf-8")
                    self._buffer = bytearray()
                else:
                    return
            else:
                return

        return self._decoder.decode(msg)


def as_dict(object):
    from datetime import datetime
    from dataclasses import is_dataclass
    from . import Enum
    from enum import Flag

    if isinstance(object, dict):
        _object = {}
        for key in object:
            if key not in ["_Client", "total_characters"]:
                if object[key] is None:
                    continue
                _object[key] = as_dict(object[key])
        return _object
    elif isinstance(object, list):
        return [as_dict(key) for key in object]
    elif is_dataclass(object):
        if object._Client:
            object._Client = None
        return object.as_dict()
    elif isinstance(object, datetime):
        return object.isoformat()
    elif isinstance(object, Enum) or isinstance(object, Flag):
        return object.value
    elif isinstance(object, bytes):
        return bytearray(object)
    elif type(object) is type:
        return None
    return object


class Serializer:
    token: str = None
    _auth_type: str = "Bot"

    def _prepare_payload(self, **kwargs):
        if "headers" not in kwargs:
            kwargs["headers"] = []
        if self.token:
            kwargs["headers"].append(("Authorization", f"{self._auth_type} {self.token}"))
        if kwargs.get("reason", None):
            kwargs["headers"].append(("X-Audit-Log-Reason", kwargs.pop("reason")))

        if not (
            type(kwargs.get("json", None)) is dict
            and kwargs.get("json", {}).get("attachments", None)
            and len(kwargs.get("json", {}).get("attachments", []))
            and all(i.file for i in kwargs.get("json", {}).get("attachments", []))
        ):
            if kwargs.get("json"):
                kwargs["headers"].append(("Content-Type", "application/json"))
            else:
                kwargs["headers"].append(("Content-Type", "text/html"))
        else:
            kwargs["data"] = aiohttp.FormData(quote_fields=False)
            files = kwargs.get("json", {}).get("attachments", [])
            _index = iter(range(len(files)))
            for file in files:
                if not file.id:
                    file.id = next(_index)
                kwargs["data"].add_field(f"files[{file.id}]", file.file, filename=file.filename or "file")

            kwargs["data"].add_field(
                "payload_json",
                ENCODER.encode(as_dict(kwargs["json"])).decode(encoding="utf-8"),
                content_type="application/json",
            )
            kwargs.pop("json")

        kwargs = self._serialize(**kwargs)
        return kwargs

    def _serialize(self, **kwargs):
        if kwargs.get("json"):
            kwargs["json"] = as_dict(kwargs["json"])
            if type(kwargs["json"]) is dict:
                for key, value in kwargs["json"].items():
                    if key in {"embeds", "components"} and type(value) is not list:
                        kwargs["json"][key] = [value]

        if kwargs.get("params"):
            for param in kwargs["params"]:
                kwargs["params"][param] = str(kwargs["params"][param])

            for i in ["before", "after", "between"]:
                if kwargs["params"].get(i, False) is None:
                    kwargs.pop(i)

        return kwargs
