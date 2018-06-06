from abc import ABCMeta, abstractmethod


class Command(metaclass=ABCMeta):

    @abstractmethod
    def execute(self, *args, **kwargs):
        pass


class Menu:
    def __init__(self):
        self.tasks = {}
        self.tasks_count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.tasks_count >= len(list(self.tasks.items())):
            raise StopIteration

        command = list(self.tasks.items())[self.tasks_count]
        self.tasks_count += 1
        return command

    @classmethod
    def add_command(cls, name, klass):
        if not name:
            raise CommandException('Command must have a name!')
        if not issubclass(klass, Command):
            raise CommandException('Class "{}" is not Command!'.format(klass))

    def execute(self, name, *args, **kwargs):
        command = self.tasks.get(name)
        if command not in Menu:
            raise CommandException('Command with name "{}" not found'.format(name))
        else:
            command.execute(args, kwargs)


class CommandException(Exception):
    def __init__(self, *args, **kwargs):
        pass


class ActionAdd(Command):
    def __init__(self, *args, **kwargs):
        pass

    def execute(self, *args, **kwargs):
        pass


class ActionFind(Command):
    def __init__(self, *args, **kwargs):
        pass

    def execute(self, *args, **kwargs):
        pass


class ActionDel(Command):
    def __init__(self, *args, **kwargs):
        pass

    def execute(self, *args, **kwargs):
        pass


class ActionStatusEnd(Command):
    def __init__(self, *args, **kwargs):
        pass

    def execute(self, *args, **kwargs):
        pass


class ActionStatusBegin(Command):
    def __init__(self, *args, **kwargs):
        pass

    def execute(self, *args, **kwargs):
        pass


class ActionChange(Command):
    def __init__(self, *args, **kwargs):
        pass

    def execute(self, *args, **kwargs):
        pass


class ActionExit(Command):
    def __init__(self, *args, **kwargs):
        pass

    def execute(self, *args, **kwargs):
        pass
