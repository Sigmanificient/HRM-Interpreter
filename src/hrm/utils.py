def require_cell(func):
    def wrapper(buffer_id):
        def inner(state):
            func(state, buffer_id)

        return inner

    return wrapper


def require_line(func):
    def wrapper(line):
        def inner(state):
            func(state, line)

        return inner

    return wrapper
