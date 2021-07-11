# mDiscord
[![Open in Visual Studio Code](https://open.vscode.dev/badges/open-in-vscode.svg)](https://open.vscode.dev/Mmesek/mdiscord)

Simple statically typed (relatively) Discord API Wrapper

`Models` & `Endpoints` are generated from documentation with a script therefore they should *in theory* provide 100% of coverage. 
Mapping is mostly 1:1 (With few additional convenience methods in `types.py`) between docs and code.

---
At this moment, usage requires slight modification to dataclasses from standard library by allowing passing additional keyword arguments to auto generated constructor
which is adding `+ ["**kwargs"]` to a second argument for _create_fn in _init_fn (Around line 532 [At least in version from January 2021])



---

Basic usage example:
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