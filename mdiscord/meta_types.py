from datetime import datetime, timedelta
from typing import Generic, TypeVar

T = TypeVar("T")


class NotSerializable(Generic[T]):
    pass


class Nullable(Generic[T]):
    pass


class UnixTimestamp(datetime):
    pass


class Duration(timedelta):
    pass
