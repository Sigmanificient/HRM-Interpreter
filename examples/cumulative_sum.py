__state = {
    'inbox': iter([1, 5, 33, 99999]),
    'outbox': [],
    'buffer': {},
    'line': 0,
    'hold': None
}


def inbox(state):
    try:
        state['hold'] = next(state['inbox'])
    except StopIteration:
        state['hold'] = 0
        state['line'] = EOF - 1


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


def jump_n(line):
    def __jump_n(state):

        if state['hold'] < 0:
            state['line'] = line - 2

    return __jump_n


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


def bump(sign, buffer_id):
    val = (sign == '+') - (sign == '-')

    def __bump(state):
        state['buffer'][buffer_id] += val
        state['hold'] = state['buffer'][buffer_id]

    return __bump


def add(buffer_id):
    def __add(state):
        state['hold'] += state['buffer'][buffer_id]

    return __add


# cumulative sum
instructions = [
    inbox,
    copy_to('e'),
    copy_to('t'),
    bump('-', 'e'),
    jump_n(9),
    add('t'),
    copy_to('t'),
    jump(4),
    copy_from('t'),
    outbox,
    jump(1)
]


EOF = len(instructions)

while __state['line'] != EOF:
    ins = instructions[__state['line']]
    ins(__state)

    __state['line'] += 1
