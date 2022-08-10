__state = {
    'inbox': iter([1]),
    'outbox': [],
    'buffer': {},
    'line': 0,
    'hold': None
}


def inbox(state):
    state['hold'] = next(state['inbox'])


def outbox(state):
    out = state.get('hold')
    if out is None:
        raise ValueError

    state['hold'] = None
    state['outbox'].append(out)
    print(state['outbox'][-1])


def jump_z(line):
    def __jump_z(state):

        if state['hold'] == 0:
            state['line'] = line - 2

    return __jump_z


def jump(line):
    def __jump(state):
        state['line'] = line - 2

    return __jump


def copy_to(buffer_id):
    def __copy_to(state):
        state['buffer'][buffer_id] = state['hold']
    return __copy_to


def copy_from(buffer_id):
    def __copy_from(state):
        state['hold'] = state['buffer'][buffer_id]

    return __copy_from


instructions = [
    inbox,
    jump_z(7),
    copy_to(0),
    outbox,
    copy_from(0),
    jump(3),
    outbox
]


EOF = len(instructions)

while __state['line'] != EOF:
    ins = instructions[__state['line']]

    ins(__state)
    __state['line'] += 1
