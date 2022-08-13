from hrm.utils import require_line


@require_line
def jump(state, line):
    state.line = line - 1


@require_line
def jump_z(state, line):
    if state.hold == 0:
        state.line = line - 1


@require_line
def jump_n(state, line):
    if state.hold < 0:
        state.line = line - 1
