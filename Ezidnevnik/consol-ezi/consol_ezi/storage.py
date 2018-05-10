import os.path as Path
import sqlite3

SQL_ADD_NAME = 'INSERT INTO task (task_name, task_description, task_status) VALUES(?,?,?)'
# SQL_ADD_DESCRIPTION = 'INSERT INTO task (task_description) VALUES (?)'
# SQL_ADD_STATUS = 'INSERT INTO task (task_status) VALUES (?)'


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

def connect(db_name=None):
    """Подкдючение к БД"""
    if db_name is None:
        db_name = ':memory:'

    conn = sqlite3.connect(db_name)
    return conn


def initialize(conn):
    """Инициализирует структуру БД. """
    script_path = Path.join(Path.dirname(__file__), 'schema.sql')

    with conn, open(script_path) as f:
        conn.executescript(f.read())


def add_name(conn, task_name, task_description, task_status):
    cursor = conn.execute(SQL_ADD_NAME, (task_name, task_description, task_status))
    return task_name, task_description, task_status


# def add_description(conn, task_description):
#     cursor = conn.execute(SQL_ADD_DESCRIPTION, (task_description,))
#     return task_description
#
#
# def add_status(conn, task_status):
#     cursor = conn.execute(SQL_ADD_STATUS, (task_status,))
#     return task_status


def find_all(conn):
    """Выводит все задачи"""
    with conn:
        cursor = conn.execute(SQL_SELECT_ALL)
        return print(cursor.fetchall())


def delete_task(conn, id):
    cursor = conn.execute(SQL_DEL_TASK, (id))


def change_status_end(conn, id):
    with conn:
        cursor = conn.execute(SQL_UPDATE_STATUS_END, (id))


def change_status_begin(conn, id):
    with conn:
        cursor = conn.execute(SQL_UPDATE_STATUS_BEGIN, (id))


def change_task(conn, id, task_name, task_description):
    with conn:
        cursor = conn.execute(SQL_UPDATE_TASK, (id, task_name, task_description))
    return id, task_name, task_description























