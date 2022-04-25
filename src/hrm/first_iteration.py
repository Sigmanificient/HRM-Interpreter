"""A first iteration to implement core mechanics."""
from sys import argv
from time import perf_counter
from typing import List, Optional, Union, Dict

State = Dict[str, Union[Optional[List[int]], Optional[int], int]]


class Instruction:

    def __init__(self, string: str):
        self.string = string

        self.method = lambda: 0
        self.args = ()

        # TODO: parse argument & slot-args
        # TODO: make a dispatcher
        if string.startswith('outbox'):
            _ins, n = string.split(' ')
            self.method = self.outbox
            self.args = (n,)

    @staticmethod
    def outbox(state, n) -> State:
        print('->', n)
        return state

    def process(self, state) -> State:
        return self.method(state, *self.args)


class Interpreter:

    def __init__(self, program, in_: Optional[List[int]] = None):
        self.state: State = {
            'in': in_ or [],
            'hold': None,
            'line': 0
        }

        self.program = [
            Instruction(line) for line in program
            if line and not line.startswith('#')
        ]

    def process(self, line):
        self.state = line.process(self.state)

    def __iter__(self):
        return self

    def __next__(self):
        if self.state['line'] >= len(self.program):
            raise StopIteration

        line = self.program[self.state['line']]
        self.state['line'] += 1
        return line


def main(*args):
    path = args[1]
    with open(path) as f:
        program = f.read().splitlines()

    marker = perf_counter()
    program = Interpreter(program)

    for line in program:
        program.process(line)

    elapsed = perf_counter() - marker
    print(f"Run is {elapsed:,.3f}s")


if __name__ == '__main__':
    main(*argv)
