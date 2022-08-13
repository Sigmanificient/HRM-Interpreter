from hrm import Interpreter
from hrm.instructions import (
    inbox, copy_to, jump_n, copy_from, add, jump, outbox, dec
)

Interpreter(
    instructions=[
        inbox,
        copy_to('e'),
        copy_to('t'),
        dec('e'),
        jump_n(8),
        add('t'),
        copy_to('t'),
        jump(3),
        copy_from('t'),
        outbox,
        jump(0)
    ],
    in_=[1, 5, 33, 99999]
).run()
