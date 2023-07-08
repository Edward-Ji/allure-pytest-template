from typing import Any


class MyObject:

    def __init__(self, value: Any=None):
        self._value: Any = value

    @property
    def value(self) -> Any:
        return self._value

    @value.setter
    def value(self, value: Any):
        self._value: Any = value

    def __str__(self):
        if self._value is None:
            return f"{type(self).__name__}()"
        return f"{type(self).__name__}({self._value})"
