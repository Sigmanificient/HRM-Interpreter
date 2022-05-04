"""A first iteration to implement core mechanics."""
from __future__ import annotations

from time import perf_counter
from typing import List, Optional, Union, Dict, Callable, Tuple

State = Dict[str, Union[Optional[int], List[int], int]]


class Instruction:

    def __init__(self, name: str):
        self.name = name

        def void(*_) -> None:
            return None

        self.method: Callable[[...], None] = void
        self.args: Tuple[Union[int, str], ...] = ()

        # TODO: parse argument & slot-args
        # TODO: make a dispatcher
        if name.startswith('outbox'):
            _ins, n = name.split(' ')
            self.method = self.outbox
            self.args = (n,)

    @staticmethod
    def outbox(state: State, n: Union[int, str]) -> State:
        print(n)
        return state

    def process(self, state: State) -> State:
        return self.method(state, *self.args)


class Interpreter:

    def __init__(self, program: List[str], in_: Optional[List[int]] = None):
        self.state: State = {
            'in': in_ or [],
            'hold': None,
            'line': 0
        }

        self.program = [
            Instruction(line) for line in program
            if line and not line.startswith('#')
        ]

    def process(self, line: Instruction):
        self.state = line.process(self.state)

    def __iter__(self) -> Interpreter:
        return self

    def __next__(self) -> str:
        if self.state['line'] >= len(self.program):
            raise StopIteration

        line: str = self.program[self.state['line']]

        self.state['line'] += 1
        return line
