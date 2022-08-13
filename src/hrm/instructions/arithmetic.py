from hrm.utils import require_cell


@require_cell
def add(state, cell_id):
    state.hold += state.memory[cell_id]


@require_cell
def sub(state, cell_id):
    state.hold -= state.memory[cell_id]


@require_cell
def inc(state, cell_id):
    state.memory[cell_id] += 1
    state.hold = state.memory[cell_id]


@require_cell
def dec(state, cell_id):
    state.memory[cell_id] -= 1
    state.hold = state.memory[cell_id]
