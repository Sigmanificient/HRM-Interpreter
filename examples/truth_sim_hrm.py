from hrm.instructions import inbox, jump_z, copy_to, outbox, copy_from, jump
from hrm.state import State


instructions = [
    inbox,
    jump_z(6),
    copy_to(0),
    outbox,
    copy_from(0),
    jump(3),
    outbox
]


__state = State([0], eof=len(instructions))


while __state.line != __state.eof:
    ins = instructions[__state.line]

    ins(__state)
    __state.line += 1
