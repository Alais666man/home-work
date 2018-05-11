import os.path as Path
import sqlite3

SQL_ADD_NAME = 'INSERT INTO task (task_name, task_description, task_status) VALUES(?,?,?)'
SQL_SELECT_ALL = '''
    SELECT
        id, task_name, task_description, task_status, created
    FROM
        task    
'''
SQL_FIND_ALL = SQL_SELECT_ALL + ' WHERE id=?'
SQL_DEL_TASK = 'DELETE FROM task WHERE id=?'
SQL_UPDATE_STATUS_END = 'UPDATE task SET task_status="Завершена" WHERE id=?'
SQL_UPDATE_STATUS_BEGIN = 'UPDATE task SET task_status="В процессе" WHERE id=?'
SQL_UPDATE_TASK = 'UPDATE task SET task_name=?, task_description=?, task_status ="В процессе" WHERE id=?'


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def connect(db_name=None):
    """Подкдючение к БД"""
    if db_name is None:
        db_name = ':memory:'

    conn = sqlite3.connect(db_name)
    conn.row_factory = dict_factory
    return conn


def initialize(conn):
    """Инициализирует структуру БД. """
    script_path = Path.join(Path.dirname(__file__), 'schema.sql')

    with conn, open(script_path) as f:
        conn.executescript(f.read())


def add_name(conn, task_name, task_description, task_status):
    """Добавляет задачу"""
    cursor = conn.execute(SQL_ADD_NAME, (task_name, task_description, task_status,))
    return task_name, task_description, task_status


def find_all(conn):
    """Выводит все задачи"""
    with conn:
        cursor = conn.execute(SQL_SELECT_ALL)
        return cursor.fetchall()


def delete_task(conn, id):
    """Удаляет задачу"""
    cursor = conn.execute(SQL_DEL_TASK, (id,))


def change_status_end(conn, id):
    """Меняет статус на завершена"""
    with conn:
        cursor = conn.execute(SQL_UPDATE_STATUS_END, (id,))


def change_status_begin(conn, id):
    """Меняет статус на в процессе"""
    with conn:
        cursor = conn.execute(SQL_UPDATE_STATUS_BEGIN, (id,))


def change_task(conn, task_name, task_description, id):
    """Редактирует задачу"""
    with conn:
        cursor = conn.execute(SQL_UPDATE_TASK, (task_name, task_description, id,))
    return task_name, task_description























