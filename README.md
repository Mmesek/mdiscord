# mDiscord
[![Open in Visual Studio Code](https://img.shields.io/static/v1?logo=visualstudiocode&label=&message=Open%20in%20Visual%20Studio%20Code&labelColor=2c2c32&color=007acc&logoColor=007acc)](https://open.vscode.dev/Mmesek/mdiscord)

[![GitHub](https://img.shields.io/github/license/Mmesek/mdiscord)](../../LICENSE.md)

[![CodeFactor Grade](https://img.shields.io/codefactor/grade/github/Mmesek/mdiscord)](https://www.codefactor.io/repository/github/mmesek/mdiscord)
![Lines of code](https://sloc.xyz/github/Mmesek/mdiscord?style=plastic)
[![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/Mmesek/mdiscord)]()
[![GitHub repo size](https://img.shields.io/github/repo-size/Mmesek/mdiscord)]()

[![Discord](https://img.shields.io/discord/517445947446525952)](https://discord.gg/z8HkfsGmrr)

Simple (relatively) typehinted Discord API Wrapper with type casting.

Made (and meant) to work in conjunction with [MFramework.py](https://github.com/Mmesek/MFramework.py) hence it's usage on it's own is rather limited (Read: It's mainly a REST wrapper with Gateway's Dispatch)

# Features
- [Generated](https://github.com/Mmesek/DocParser) 1:1 Mapping of [models](mdiscord/types/models.py) & [endpoints](mdiscord/http/endpoints.py) based on Discord [documentation](https://github.com/discord/discord-api-docs). All endpoints are available as methods of `Client`.
- *In theory* 100% of documented API coverage. 
- Iterating prioritizable event [listeners](mdiscord/utils/utils.py) supporting predicates without blocking them.
- [Differentiating](mdiscord/opcodes.py) direct messages from guild messages by prependeding them with `DIRECT_`.
- Automatic [skipping](mdiscord/opcodes.py) of events sent by bots (Those containing `is_bot` attribute set to `True`)
- [Embed](mdiscord/types/types.py) builder respecting message limits without throwing.
- Convenience methods for models in [`types.py`](mdiscord/types/types.py).
- Just a simple API wrapper with Gateway client without anything fancy, really.

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
