import time


def pause(sec):
    def decorator(func):
        def wrapper(*args, **kwargs):
            time.sleep(int(sec))
            result = func(*args, **kwargs)
            print('Фунция выполняется с задержкой {:f} секунды!'.format(sec))
            return result
        return wrapper
    return decorator
