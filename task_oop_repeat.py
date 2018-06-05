from abc import ABCMeta, abstractmethod
import json
import pickle
import os


class ParamHandler(metaclass=ABCMeta):

    def __init__(self, source):
        self.source = source
        self.params = {}

    def add_param(self, key, value):
        self.params[key] = value

    def get_all_params(self):
        return self.params

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self):
        pass

    types = {}

    @classmethod
    def add_type(cls, name, klass):
        if not name:
            raise ParamHandlerException('Type must have a name!')
        if not issubclass(klass, ParamHandler):
            raise ParamHandlerException('Class "{}" is not ParamHandler!'.format(klass))
        cls.types[name] = klass

    @classmethod
    def get_instance(cls, source, *args, **kwargs):
        # Шаблон "Factory Method"
        _, ext = os.path.splitext(str(source).lower())
        ext = ext.lstrip('.')
        klass = cls.types.get(ext)
        if klass is None:
            raise ParamHandlerException('Type "{}" not found!'.format(ext))
        return klass(source, *args, **kwargs)


def new_type(type):
    def decorator(cls):
        ParamHandler.add_type(cls, type)
        return cls
    return decorator


class ParamHandlerException(Exception):
    pass


@new_type('txt')
class TextParamHandler(ParamHandler):
    def read(self):
        """Чтение из текстового файла"""
        with open(self.source) as f:
            self.params = [a for a in f.readline().split(':')]

    def write(self):
        """Запись в текстовый файл"""
        with open(self.source, 'w') as f:
            for a in self.params:
                f.write('{}:{}\n'.format(a, self.params[a]))


@new_type('json')
class JsonParamHandler(ParamHandler):
    def read(self):
        """Чтение из json файла и присвоение значений в self.params"""
        with open(self.source) as f:
            self.params = json.load(f)

    def write(self):
        """Запись в текстовый файл параметров self.params"""
        with open(self.source, 'w') as f:
            json.dump(self.params, f, indent=4)


@new_type('pickle')
class PickleParamHandler(ParamHandler):
    def read(self):
        """Чтение в формате Pickle и присвоение значений в self.params"""
        with open(self.source) as f:
            self.params = pickle.load(f)

    def write(self):
        """Запись в формате Pickle параметров self.params"""
        with open(self.source, 'w') as f:
            pickle.dump(self.params, f)


if __name__ == '__main__':
    config = ParamHandler.get_instance('./params.json')
    config.add_param('key1', 'val1')
    config.add_param('key2', 'val2')
    config.add_param('key3', 'val3')
    config.write()
    config = ParamHandler.get_instance('./params.json')
    config.read()  # читаем данные из текстового файла
    print(config.params)
