from hrm import Interpreter
from hrm.instructions import inbox, jump_z, copy_to, outbox, copy_from, jump


Interpreter(
    instructions=[
        inbox,
        jump_z(6),
        copy_to(0),
        outbox,
        copy_from(0),
        jump(3),
        outbox
    ],
    in_=[0]
).run()
