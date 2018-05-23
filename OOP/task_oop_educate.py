from abc import ABCMeta, abstractmethod



"""
Три класса:
1. Kurs - курсы
2. Teachers - учителя
3. Students - ученики
4. Lessons - занятия на курсах  

Kurs является абстрактным классом
Каждый предмет привязан к определённому преподователю. Ученики привязаны к определённым предметам. 
Т.е. класс Lessons наследуется от Teachers, Students наследуется от Lessons

"""


class Kurs(metaclass=ABCMeta):
    @abstractmethod
    def lesson(self):
        pass

    @abstractmethod
    def teacher(self):
        pass


class Teachers(Kurs):
    def lesson(self):
        pass

    def teacher(self):
        pass

    @classmethod
    def add_teacher(self, fullname, lesson):
        pass



class Lessons(Kurs):




class students(Lessons):
    @classmethod
    def add_student(self):
        pass

    @classmethod
    def del_student(self):
        pass



