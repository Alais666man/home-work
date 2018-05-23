class Config(object):                                       # Создаётся класс Config
    __slots__ = ()

    def __init__(self, file_size, file_direction, etc):
        self.__file_size = file_size
        self.__file_direction = file_direction

    @classmethod
    def get_info(self, config_file):
        with open('config_file') as f:                      # Получение инфо-ии из конфиг файла
            info = f.readline()
            return self.__info

    @classmethod
    def give_info(self, config_file):
        with open('config_file', 'w') as f:                 # Внесение инфо-ии в конфиг файла
            info = f.write()
            return self.get_info.append(info)


class TypeConfig(Config):                                   # Создаётся класс-потомок
    __slots__ = ('__type',)

    def __init__(self, file_size, file_direction, type):
        super().__init__(file_size, file_direction, etc)
        self.__type = type

    @classmethod
    def check_type(self):                                   # Проверка всех поддерживаемых форматов
        # return fetchall???

    @classmethod
    def add_type(self):
        if type not in self.__type:                         # Добавление нового формата
            self.check_type.append(type)

    @classmethod
    def del_type(self):
        if type in self.check_type():                       # Удаление формата
            self.check_type().remove(type)


"""
Изначально создаём класс Config, который отвечает за запись и чтение информации из файла
Его аргументам являются размер файла, его постоположение, ...
Класс TypeConfig отвечает за определение типа формата файла и в его методы входят:
 - проверка самого формата
 - добавление поддержки новых форматов
 - удаление форматов
 Аргументами TypeConfig являются те же аргументы, что и в Config, (класс - родитель) и аргумент type
 Методы класса TypeConfig являются статическими и привязаны только к данному классу 
"""