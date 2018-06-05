from abc import ABCMeta, abstractmethod
from datetime import datetime

import re


class Validator(metaclass=ABCMeta):
    def __init__(self, value):
        self.value = value

    @abstractmethod
    def validate(self):
        pass

    value = {}

    @classmethod
    def add_type(cls, name, klass):
        # Validator.add_type('email')
        if not name:
            raise ValidatorException('Validator must have a name!')
        if not issubclass(klass, Validator):
            raise ValidatorException('Class "{}" is not Validator!'.format(klass))
        cls.value[name] = klass

    @classmethod
    def get_instance(cls, name):
        Validator.get_instance(name)
        if not name:
            raise ValidatorException('Validator with name "{}" not found'.format(name))
        return


class ValidatorException(Exception):
    """Класс исключения Validator'a"""


def new_value(name):
    def decorator(cls):
        Validator.add_type(cls, name)
        return cls
    return decorator


@new_value('email')
class EmailValidator(Validator):
    def validate(self):
        if re.search("[@]", self.value) is None:
            return False
        else:
            return True


@new_value('datetime')
class DateTimeValidator(Validator):
    def validate(self):
        if datetime != datetime.strptime('value', '%Y-%M-%D').strptime('value', '%Y-%M-%D %H:%M')\
                .strptime('value', '%Y-%M-%D %H:%M:%S').strptime('value', '%D.%M.%Y')\
                .strptime('value', '%D.%M.%Y %H:%M').strptime('value', '%D.%M.%Y %H:%M:%S')\
                .strptime('value', '%D/%M/%Y').strptime('value', '%D/%M/%Y %H:%M')\
                .strptime('value', '%D/%M/%Y %H:%M:%S'):
            return False
        else:
            return True







