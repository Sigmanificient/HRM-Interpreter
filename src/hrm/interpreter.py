"""A first iteration to implement core mechanics."""

from __future__ import annotations

from typing import List, Optional

from .state import State


class Interpreter:

    def __init__(self, instructions, in_: Optional[List[int]] = None):
        self.instructions = instructions
        self.state: State = State(in_, eof=len(instructions))

    def run(self):
        while self.state.line != self.state.eof:
            ins = self.instructions[self.state.line]
            ins(self.state)

            self.state.line += 1
