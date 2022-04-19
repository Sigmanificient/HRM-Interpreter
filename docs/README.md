# Human Resource Machine Interpreter

<img src="assets/game.png" alt="Game img">

Human Resource Machine is a game where you play an employee controlled by a block-like "programming language".
The goal of this repository is to create an interpreter for this "programming language".

The syntax is kind of clause to assembly, using jumps for controlling the flow.
The inbox and outbox correspond to argument and return value.
For each level, a prompt is given and the player code is tested with multiple values.

Overflow occurs when the value is lower than -999 or bigger than 999.

## HRM interpreted Language

The HRM language will follow these specificities:

- Comment will be defined using `#` on an empty line.
- `inbox` will give an integer value from a given stack ranging from -999 to 999
- `outbox` will be yield from the `run` function.
- every value within square bracket will be considered as a number corresponding to a slot id, or a label that identify a slot.
- `jump` will have an argument to the instruction to teleport the pointer to. blank & comment line will not count.
- `slot` allow to define slot name given an id and a string.

### calling a program

This function is will work only with a string. 
To load from a file, use `run_file`

`run` signature
```py
def run(
    program: str,                     # The string of the program
    inbox: List[int],                 # The inbox content
    slots: int = 0,                   # The number of slots available
    remove_int_limit: bool = False    # Remove [-999, 999] Hrm Int limit
) -> Generator[str]:
    ...
```

An example of what the interpreted language will look like with arrow, to make the program more readable.

<img src="assets/subl.png">
