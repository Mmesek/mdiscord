# mDiscord
Simple statically typed (relatively) Discord API Wrapper

`Models` & `Endpoints` are generated from documentation with a script therefore they should *in theory* provide 100% of coverage. 
Mapping is mostly 1:1 (With few additional convenience methods in `types.py`) between docs and code.

---
At this moment, usage requires slight modification to dataclasses from standard library by allowing passing additional keyword arguments to auto generated constructor
which is adding `+ ["**kwargs"]` to a second argument for _create_fn in _init_fn (Around line 532 [At least in version from January 2021])