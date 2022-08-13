from string import ascii_uppercase
from typing import Any


class Char(str):
    CHARSET = ascii_uppercase
    OFFSET_INDEX = ord(CHARSET[0])
    CHAR_LEN = len(CHARSET)

    @classmethod
    def from_int(cls, value: int):
        return Char(cls.CHARSET[value % cls.CHAR_LEN])

    @property
    def _index(self) -> int:
        return ord(self) - self.OFFSET_INDEX

    def __add__(self, other: Any) -> str:
        if not isinstance(other, Char):
            raise TypeError(f'Cannot add {type(self)} to {type(other)}')

        return Char.from_int(self._index + other._index)

    def __sub__(self, other: Any) -> str:
        if not isinstance(other, Char):
            raise TypeError(f'Cannot subtract {type(self)} from {type(other)}')

        return Char.from_int(self._index + other._index)

    def increment(self):
        return Char.from_int(self._index + 1)

    def decrement(self):
        return Char.from_int(self._index - 1)
