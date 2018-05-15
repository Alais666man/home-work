from functools import lru_cache
import hashlib


def make_token(username, password):
    with open('token.txt', 'w') as f:
        s = username + password
        return f.write(hashlib.md5(s.encode()).hexdigest())


make_token(username=input(), password=input())


@lru_cache(maxsize=None)
def login_required(username, password):
    def decorator(func):

        def wrapper(*args, **kwargs):
            with open('token.txt') as f:
                hash = f.read()
                result = func(*args, **kwargs)
                t = 0
                while t < 3:
                    username = input()
                    password = input()
                    s = username + password
                    if hash != hashlib.md5(s.encode()).hexdigest():
                        print('Функция защищена паролем')
                        t += 1
                    else:
                        return result
        return wrapper




