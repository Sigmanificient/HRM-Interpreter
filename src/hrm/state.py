from typing import List, Optional


class State:
    __slots__ = ('inbox', 'hold', 'line', 'eof', 'memory')

    def __init__(self, inbox=None, eof: int = 0):
        self.inbox = iter(inbox or [])
        self.hold = None

        self.memory = {}

        self.line: int = 0
        self.eof: int = eof
