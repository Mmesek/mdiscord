# -*- coding: utf-8 -*-
'''
Discord Exceptions
----------

Discord Exceptions.

:copyright: (c) 2021 Mmesek

'''

class Insufficient_Permissions(Exception):
    pass

class RequestError(Exception):
    pass

class BadRequest(RequestError):
    pass

class JsonBadRequest(BadRequest):
    pass
