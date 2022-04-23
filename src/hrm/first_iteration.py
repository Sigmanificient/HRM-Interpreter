"""A first iteration to implement core mechanics."""


class Interpreter:

    def __init__(self, program):
        self.line = 0
        self.program = program

    def __iter__(self):
        return self

    def __next__(self):
        if self.line >= len(self.program):
            raise StopIteration

        line = self.program[self.line]
        self.line += 1
        return line


def main():
    with open('prog_1.hrm') as f:
        program = f.read().splitlines()

    program = Interpreter(program)

    for line in program:
        print(line)


if __name__ == '__main__':
    main()
