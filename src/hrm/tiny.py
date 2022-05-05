from __future__ import annotations

from typing import Any


class Tiny:
    LIMIT_SIZE = 999

    def __check_boundaries(self) -> Tiny:
        """ Check if the value is within the game's int boundaries."""
        if self.__value < -self.LIMIT_SIZE or self.__value > self.LIMIT_SIZE:
            raise ValueError(f'Tiny value must be between {-self.LIMIT_SIZE} and {self.LIMIT_SIZE}')
        return self

    def __init__(self, value: int):
        self.__value = value
        self.__check_boundaries()

    def __repr__(self) -> str:
        return repr(self.__value)

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Tiny):
            raise TypeError('Only Tiny objects can be compared')

        return self.__value == other.__value

    def __add__(self, other: Any) -> Tiny:
        """ Addition of two Tiny objects. """
        if not isinstance(other, Tiny):
            raise TypeError('Only Tiny objects can be added')

        return Tiny(self.__value + other.__value)

    def __sub__(self, other: Any) -> Tiny:
        """ Subtraction of two Tiny objects. """
        if not isinstance(other, Tiny):
            raise TypeError('Only Tiny objects can be subtracted')

        return Tiny(self.__value - other.__value)

    def increment(self) -> Tiny:
        """ Increment the Tiny object by 1. """
        self.__value += 1
        return self.__check_boundaries()

    def decrement(self) -> Tiny:
        """ Decrement the Tiny object by 1. """
        self.__value -= 1
        return self.__check_boundaries()
