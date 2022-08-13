from typing import List, Optional

from hrm.types import Tiny


class State:
    __slots__ = ('inbox', 'hold', 'line', 'eof', 'memory')

    def __init__(self, inbox: List[Tiny] = None, eof: int = 0):
        self.inbox: List[Tiny] = iter(inbox or [])
        self.hold: Optional[Tiny] = None

        self.memory = {}

        self.line: int = 0
        self.eof: int = eof
