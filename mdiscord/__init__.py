# -*- coding: utf-8 -*-
"""
Discord API
----------

Discord API.

:copyright: (c) 2020 Mmesek
"""

from mdiscord.exceptions import *  # noqa: F401
from mdiscord.http.client import HTTP_Client as REST  # noqa: F401
from mdiscord.types import *  # noqa: F401
from mdiscord.websocket import Client, onDispatch  # noqa: F401


@onDispatch
async def ready(self: Client, ready: Ready):
    self.user_id = ready.user.id
    self.username = ready.user.username
    self.resume_url = ready.resume_gateway_url
    self.session_id = ready.session_id
    from .utils.utils import log

    log.info("Connected as %s", ready.user.username)
