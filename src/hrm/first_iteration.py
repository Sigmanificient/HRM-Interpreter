"""A first iteration to implement core mechanics."""


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
    def outbox(n):
        print(n)

    def process(self):
        print('->', self.string)
        self.method(*self.args)


class Interpreter:

    def __init__(self, program):
        self.line = 0
        self.program = [
            Instruction(line) for line in program
            if line and not line.startswith('#')
        ]

    def __iter__(self):
        return self

    def __next__(self):
        if self.line >= len(self.program):
            raise StopIteration

        line = self.program[self.line]
        self.line += 1
        return line


def main():
    with open('outbox.hrm') as f:
        program = f.read().splitlines()

    program = Interpreter(program)

    for line in program:
        line.process()


if __name__ == '__main__':
    main()
