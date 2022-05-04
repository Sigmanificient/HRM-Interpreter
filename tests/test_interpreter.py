import io
from contextlib import redirect_stdout
from src.hrmi.first_iteration import Interpreter


def test_comments():
    interpreter = Interpreter(['# a comment', '#'])
    assert len(interpreter.program) == 0


def test_outbox():
    program = Interpreter(['outbox 1', 'outbox 2'])

    f = io.StringIO()
    with redirect_stdout(f):
        for line in program:
            program.process(line)

    out = f.getvalue()
    assert out == '-> 1\n-> 2\n'
