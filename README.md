# mDiscord
[![Open in Visual Studio Code](https://open.vscode.dev/badges/open-in-vscode.svg)](https://open.vscode.dev/Mmesek/mdiscord)

Simple typehinted (relatively) Discord API Wrapper with type casting.

`Models` & `Endpoints` are generated from documentation with a script therefore they should *in theory* provide 100% of coverage. 
Mapping is mostly 1:1 (With few additional convenience methods in `types.py`) between docs and code.

---
At this moment, usage requires slight modification to dataclasses from standard library by allowing passing additional keyword arguments to auto generated constructor
which is adding `+ ["**kwargs"]` to a second argument for _create_fn in _init_fn (Around line 532 [At least in version from January 2021])



---

Basic (Websocket) usage example:
```python
cfg = {
    "DiscordTokens": {
        "Bot": "TOKEN"
    }
}

from mdiscord import onDispatch, Message, Client

@onDispatch
async def message_create(ctx: Client, msg: Message):
    pass

async def main():
    client = Client("Bot", cfg, None, None)
    while True:
        async with client:
            await client.receive()

import asyncio
asyncio.run(main())
```

---

HTTP only (REST) usage example:
```python
from mdiscord.http_client import HTTP_Client
import asyncio

webhook_id = 0
webhook_token = ""

async def main():
    e = HTTP_Client()
    await e.execute_webhook(webhook_id, webhook_token, content="Hello")

asyncio.run(main())
```