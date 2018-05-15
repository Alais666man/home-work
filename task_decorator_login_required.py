from functools import lru_cache
import hashlib


def make_token(username, password):
    with open('token.txt', 'w') as f:
        s = username + password
        return f.write(hashlib.md5(s.encode()).hexdigest())


def login_required(func):
    @lru_cache(maxsize=None)
    def wrapped(*args, **kwargs):
        result = func(*args, **kwargs)
        with open('token.txt') as f:
            token = f.read()
        count = 0
        while count < 3:
            username = input()
            password = input()
            user = hashlib.md5((username + password).encode()).hexdigest()
            if user != token:
                print('Функция защищена паролем')
                count += 1
            else:
                return result
    return wrapped




# def summa(a, b):
#     return print(a + b)
#
# print(summa(2, 1))










# @login_required
#





    # def decorator(func):
    #
    #     def wrapper(*args, **kwargs):
    #         with open('token.txt') as f:
    #             hash = f.read()
    #             result = func(*args, **kwargs)
    #             t = 0
    #             while t < 3:
    #                 username = input()
    #                 password = input()
    #                 s = username + password
    #                 if hash != hashlib.md5(s.encode()).hexdigest():
    #                     print('Функция защищена паролем')
    #                     t += 1
    #                 else:
    #                     return result
    #     return wrapper
    # return decorator










# def login_required(username, password):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             result = func(*args, **kwargs)
#             user = hashlib.md5((username + password).encode()).hexdigest()
#             t = 0
#             while t < 3:
#                 with open('token.txt') as f:
#                     token = f.read()
#                 if user != token:
#                     print('Функция защищена паролем')
#                     t += 1
#                 else:
#                     return result
#             return wrapper
#         return decorator