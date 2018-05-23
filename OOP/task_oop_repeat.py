from abc import ABCMeta, abstractmethod
import json
import pickle


class ParamHandler(metaclass=ABCMeta):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self):
        pass


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

    @classmethod
    def get_instance(cls, source):
        _,ext = os.path.splitext(str(source).lower())
        if ext == '.json':
            return JsonParamHandler(source)
        return PickleParamHandler(source)


class TextParamHandler(ParamHandler):
    def read(self):
        """Чтение из текстового файла"""
        with open('file_name') as f:
            f.read()

    def write(self):
        """Запись в текстовый файл"""
        with open('text_test.txt' 'w') as f:
            f.write()


class JsonParamHandler(ParamHandler):
    def read(self):
        """Чтение из json файла и присвоение значений в self.params"""
        with open('') as f:
            self.params = json.load()

    def write(self):
        """Запись в текстовый файл параметров self.params"""
        with open('', 'w') as f:
            json.dump()
#
#
# class PickleParamHandler(ParamHandler):
#     def read(self):
#         """Чтение в формате Pickle и присвоение значений в self.params"""
#         with open('') as f:
#             self.params = f.read()
#
#     def write(self):
#         """Запись в формате XML параметров self.params"""
#         with open('', 'w') as f:


 class ParamHandler(metaclass=ABCMeta):
     types = {}

     @classmethod
     def add_type(cls, name, klass):
         if not name:
             raise ParamHandlerException('Type must have a name!')

     if not issubclass(klass, ParamHandler):
         raise ParamHandlerException(
             'Class "{}" is not ParamHandler!'.format(klass)
         )
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


 # config = ParamHandler.get_instance('./params.xml')
 # config.add_param('key1', 'val1')
 # config.add_param('key2', 'val2')
 # config.add_param('key3', 'val3')
 # config.write()  # запись файла в XML формате
 # config = ParamHandler.get_instance('./params.txt')
 # config.read()  # читаем данные из текстового файла

 if __name__ == '__main__':
     config = ParamHandler.get_instance('./params.json')