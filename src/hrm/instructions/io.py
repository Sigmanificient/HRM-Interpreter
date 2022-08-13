def inbox(state):
    try:
        state.hold = next(state.inbox)

    except StopIteration:
        state.hold = None
        state.line = state.eof - 1


def outbox(state):
    out = state.hold
    print(out)

    state.hold = None
