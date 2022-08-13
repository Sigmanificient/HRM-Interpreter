from hrm import Interpreter
from hrm.instructions import inbox


def test_inbox():
    program = Interpreter([inbox], in_=[1])
    program.run()

    assert program.state.hold == 1

    program = Interpreter([inbox], in_=[1, 2])
    program.run()

    assert program.state.hold == 1

    program = Interpreter([inbox, inbox], in_=[1, 2, 3])
    program.run()

    assert program.state.hold == 2

    program = Interpreter([inbox], in_=[])
    program.run()

    assert program.state.hold is None

    program = Interpreter([inbox, inbox, inbox], in_=[1])
    program.run()

    assert program.state.hold is None
