from hrm.utils import require_cell


@require_cell
def copy_to(state, cell_id):
    state.memory[cell_id] = state.hold


@require_cell
def copy_from(state, cell_id):
    state.hold = state.memory[cell_id]
