def require_cell(func):
    def wrapper(buffer_id):
        def inner(state):
            func(state, buffer_id)

        inner.__name__ = func.__name__
        return inner
    return wrapper


def require_line(func):
    def wrapper(line):
        def inner(state):
            func(state, line - 1)

        inner.__name__ = func.__name__
        return inner

    return wrapper
