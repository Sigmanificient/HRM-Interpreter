import pathlib
from sys import argv

from hrm import parser


def main():
    if len(argv) < 2:
        print("No program provided !")
        return

    path = argv[1]    

    program = pathlib.Path(path).read_text()
    parser.parse(program)


if __name__ == '__main__':
    main()
