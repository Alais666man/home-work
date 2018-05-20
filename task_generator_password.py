import random
import string


def password_generator(n):
    while True:

        yield ''.join(random.sample(string.ascii_uppercase + string.ascii_lowercase
                         + string.digits + string.punctuation, n))


