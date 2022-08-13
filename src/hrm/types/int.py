from __future__ import annotations


class Int(int):

    def increment(self) -> Int:
        """ Increment the Tiny object by 1. """
        return Int(self + 1)

    def decrement(self) -> Int:
        return Int(self - 1)
