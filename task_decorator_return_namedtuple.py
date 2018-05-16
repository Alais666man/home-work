from collections import namedtuple


def return_namedtuple(*names):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if isinstance(result, tuple):
                name_tuple = namedtuple('name_tuple', list(*names))
                return name_tuple(*result)
        return wrapper
    return decorator







