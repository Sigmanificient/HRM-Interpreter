from sys import argv
from interpreter import Interpreter



def main():
    if len(argv) < 2:
        print("No program provided !")
        return

    path = argv[1]    

    with open(path) as f:
        program = Interpreter(f.read().splitlines())
 
    for line in program:
        program.process(line)


if __name__ == '__main__':
    main()
