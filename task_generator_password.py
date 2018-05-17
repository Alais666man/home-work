import random, string


def password_generator(n):
    while True:
        parol = ''
        yield parol.join(random.sample(string.ascii_uppercase + string.ascii_lowercase
                         + string.digits + string.punctuation, n))


