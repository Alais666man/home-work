from abc import ABCMeta, abstractmethod
import re


class Validator(metaclass=ABCMeta):
    def init(self, value):
        self.value = value

    @abstractmethod
    def validate(self, value):
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
    def get_instance(cls, name, *args, **kwargs):
        klass = cls.value.get(name)
        if klass is None:
            raise ValidatorException('Validator with name "{}" not found'.format(name))
        return klass(*args, **kwargs)


class ValidatorException(Exception):
    def init(self, ext):
        pass


def new_value(name):
    def decorator(cls):
        Validator.add_type(name, cls)
        return cls
    return decorator


@new_value('email')
class EmailValidator(Validator):
    def validate(self, value):
        if re.search("[@]", value) is None:
            return False
        else:
            return True


@new_value('datetime')
class DateTimeValidator(Validator):
    def validate(self, value):
        if re.search("((\d{,4}[./-]\d{,2}[./-]\d{,4} ?\d?\d?:?\d?\d?:?\d?\d))", value) is None:
            return False
        else:
            return True







