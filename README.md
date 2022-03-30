# mDiscord
[![Open in Visual Studio Code](https://open.vscode.dev/badges/open-in-vscode.svg)](https://open.vscode.dev/Mmesek/mdiscord)

Simple typehinted (relatively) Discord API Wrapper with type casting.

[`Models`](mdiscord/models.py) & [`Endpoints`](mdiscord/endpoints.py) are generated from [documentation](https://github.com/discord/discord-api-docs) with a [script](https://github.com/Mmesek/DocParser) therefore they should *in theory* provide 100% of coverage. 

Mapping is mostly 1:1 (With few additional convenience methods in [`types.py`](mdiscord/types.py)) between docs and code.

Wrapper was made (and meant) to work with conjunction with [MFramework.py](https://github.com/Mmesek/MFramework.py) hence it's usage on it's own is rather limited (Read: It's mainly a REST wrapper with Gateway's Dispatch).



# Examples

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

# Contributing

While PR's are welcome, for command-related capability contributions, visit [MFramework.py](https://github.com/Mmesek/MFramework.py) repo.
