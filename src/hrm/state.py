from typing import List, Optional

from hrm.tiny import Tiny


class State:
    __slots__ = ('inbox', 'hold', 'line')

    def __init__(self, inbox: List[Tiny] = None):
        self.inbox: List[Tiny] = inbox or []
        self.hold: Optional[Tiny] = None
        self.line: int = 0


