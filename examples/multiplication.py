import logging

from hrm import Interpreter
from hrm.instructions import (
    inbox, copy_to, jump_z, dec, jump_n, copy_from, add, jump, outbox, sub
)


logging.basicConfig(level=logging.DEBUG)


Interpreter(
    instructions=[
        inbox,
        copy_to('y'),
        inbox,
        jump_z(14),
        copy_to('x'),
        copy_to('result'),

        dec('y'),
        jump_n(16),
        jump_z(13),

        copy_from('result'),
        add('x'),
        copy_to('result'),

        jump(6),
        copy_from('result'),

        outbox,
        jump(0),
        copy_from('result'),
        sub('result'),
        jump(14)
    ],
    in_=[42, 69]
).run()
