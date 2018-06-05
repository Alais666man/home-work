from abc import ABCMeta, abstractmethod


class Command(metaclass=ABCMeta):

    @abstractmethod
    def execute(self, *args, **kwargs):
        pass


class Menu:
    def __init__(self, name, klass):
        self.name = name
        self.klass = klass

    @classmethod
    def add_command(cls, name, klass):
        if not name:
            raise CommandException('Command must have a name!')
        if not issubclass(klass, Command):
            raise CommandException('Class "{}" is not Command!'.format(klass))

    @classmethod
    def execute(cls, name, *args, **kwargs):
        if name not in Menu:
            raise CommandException('Command with name "{}" not found'.format(name))

    def __iter__(self):
        pass

    def __next__(self):
        pass


class ActionAdd(Command):
    def __init__(self, *args, **kwargs):
        pass

    def execute(self):
        """Добавляем задачу"""
        task_name = input('\nВведите имя задачи: ')
        task_description = input('\nВведите текст задачи: ')
        task_status = 'В процессе'
        with get_connection() as conn:
            name = storage.add_name(conn, task_name, task_description, task_status)
        action_find_all()
        main()


class ActionFind(Command):
    def __init__(self, *args, **kwargs):
        pass

    def execute(self):
        """Вывести все задачи"""
        with get_connection() as conn:
            tasks = storage.find_all(conn)

            template = '{task[id]}/ {task[task_name]} => {task[task_description]} | {task[task_status]} | {task[created]} |'
            for task in tasks:
                print(template.format(task=task))
        main()


class ActionDel(Command):
    def __init__(self, *args, **kwargs):
        pass

    def execute(self):
        """Удалить задачу"""
        id = input('\nВведите id задачи для удаления: ')
        with get_connection() as conn:
            delete = storage.delete_task(conn, id)
        action_find_all()
        main()


class ActionStatusEnd(Command):
    def __init__(self, *args, **kwargs):
        pass

    def execute(self):
        """Изменить статус на завершена"""
        id = input('\nВведите id задачи: ')
        # task_status = 'Завершена'
        with get_connection() as conn:
            status = storage.change_status_end(conn, id)
        action_find_all()
        main()


class ActionStatusBegin(Command):
    def __init__(self, *args, **kwargs):
        pass

    def execute(self):
        """Изменить статус на в процессе"""
        id = input('\nВведите id задачи: ')
        # task_status = 'Завершена'
        with get_connection() as conn:
            status = storage.change_status_begin(conn, id)
        action_find_all()
        main()


class ActionChange(Command):
    def __init__(self, *args, **kwargs):
        pass

    def execute(self):
        """Отредактировать задачу"""
        id = input('\nВведите id задачи: ')
        task_name = input('\nВведите имя задачи: ')
        task_description = input('\nВведите текст задачи: ')
        with get_connection() as conn:
            task = storage.change_task(conn, task_name, task_description, id)
        action_find_all()
        main()


class ActionExit(Command):
    def __init__(self, *args, **kwargs):
        pass

    def execute(self):
        """Выйти"""
        sys.exit(0)