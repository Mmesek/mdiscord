# -*- coding: utf-8 -*-
"""
Discord API
----------

Base Types.

:copyright: (c) 2021-2024 Mmesek
"""

from typing import TYPE_CHECKING, Any, Optional, get_type_hints

import msgspec

from mdiscord.types.meta import NotSerializable
from mdiscord.utils.serializer import from_builtins, to_builtins

if TYPE_CHECKING:
    from mdiscord.websocket.websocket import WebSocket_Client as Bot
else:
    # NOTE: Hack of sorts as otherwise `_decoder` in `Deserializer` throws `NameError`
    from mdiscord.utils.serializer import Serializer as Bot


class DiscordObject(msgspec.Struct, kw_only=True, omit_defaults=True):
    _Client: NotSerializable[Optional["Bot"]] = msgspec.UNSET

    def as_dict(self) -> dict[str, Any]:
        """
        Example
        -------
        >>> from mdiscord import Message
        >>> Message(channel_id=123).as_dict()
        {'channel_id': 123}
        """
        return {
            k: v
            for k, v in msgspec.to_builtins(self, enc_hook=to_builtins).items()
            if getattr(get_type_hints(self.__class__, include_extras=True)[k], "__metadata__", [()])[0]
            != "not_serializable"
        }

    @classmethod
    def from_dict(cls, **kwargs):
        """
        Example
        -------
        >>> class Message(DiscordObject):
        ...     channel_id: int
        >>> Message.from_dict(**{"channel_id": 123})
        Message(channel_id=123, _Client=UNSET)
        """
        return msgspec.convert(kwargs, cls, dec_hook=from_builtins)
