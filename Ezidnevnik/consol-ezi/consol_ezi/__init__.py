import sys

from consol_ezi import storage

get_connection = lambda: storage.connect('task.sqlite')


def main():
    with get_connection() as conn:
        storage.initialize(conn)
    action_show_menu()

    actions = {
        '1': action_add,
        '2': action_find_all,
        '3': action_del,
        '4': action_status_end,
        '5': action_status_begin,
        '6': action_change,
        'q': action_exit
    }
    while 1:
        cmd = input('Введите команду: ')
        action = actions.get(cmd)

        if action:
            action()
        else:
            print('Не известная команда')


def action_show_menu():
    """Показать меню"""
    print('''
1. Добавить задачу
2. Список задач
3. Удалить задачу
4. Завершить задачу
5. Начать задачу снова
6. Редактировать задачу
q. Выйти
''')


def action_add():
    """Добавляем задачу"""
    task_name = input('\nВведите имя задачи: ')
    task_description = input('\nВведите текст задачи: ')
    task_status = 'В процессе'
    with get_connection() as conn:
        name = storage.add_name(conn, task_name, task_description, task_status)
    action_find_all()
    main()


def action_find_all():
    """Вывести все URL-адреса"""
    with get_connection() as conn:
        tasks = storage.find_all(conn)

        template = '{task[id]}/ {task[task_name]} => {task[task_description]} | {task[task_status]} | {task[created]} |'
        for task in tasks:
            print(template.format(task=task))
    main()


def action_del():
    id = input('\nВведите id задачи для удаления: ')
    with get_connection() as conn:
        delete = storage.delete_task(conn, id)
    action_find_all()
    main()


def action_status_end():
    id = input('\nВведите id задачи: ')
    # task_status = 'Завершена'
    with get_connection() as conn:
        status = storage.change_status_end(conn, id)
    action_find_all()
    main()


def action_status_begin():
    id = input('\nВведите id задачи: ')
    # task_status = 'Завершена'
    with get_connection() as conn:
        status = storage.change_status_begin(conn, id)
    action_find_all()
    main()


def action_change():
    id = input('\nВведите id задачи: ')
    task_name = input('\nВведите имя задачи: ')
    task_description = input('\nВведите текст задачи: ')
    with get_connection() as conn:
        task = storage.change_task(conn, task_name, task_description, id)
    action_find_all()
    main()


def action_exit():
    """Выйти"""
    sys.exit(0)