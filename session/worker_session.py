from data import *
from datetime import *


# Проверка работает ли сейчас сотрудник
def worker_session_status(worker_id):
    try:
        max_rw = WORKERS_SHEET.max_row
        for i in range(max_rw):
            if str(WORKERS_SHEET[f'C{i+1}'].value) == str(worker_id) and str(WORKERS_SHEET[f'D{i+1}'].value) == str('Да'):
                return True
            elif str(WORKERS_SHEET[f'C{i+1}'].value) == str(worker_id) and str(WORKERS_SHEET[f'D{i+1}'].value) == str('Нет'):
                return False
    except Exception as e:
        print(f'worker_session Строка №15 - {e}')


# Функция запуска смены
def worker_start_session(worker_id):
    try:
        max_rw = WORKERS_SHEET.max_row
        for i in range(max_rw):
            if str(WORKERS_SHEET[f'C{i+1}'].value) == str(worker_id):
                WORKERS_SHEET[f'D{i+1}'] = 'Да'
        save_data()
    except Exception as e:
        print(f'worker_session Строка №27 - {e}')


# Функция остановки смены
def worker_end_session(worker_id):
    try:
        max_rw = WORKERS_SHEET.max_row
        for i in range(max_rw):
            if str(WORKERS_SHEET[f'C{i+1}'].value) == str(worker_id):
                WORKERS_SHEET[f'D{i+1}'] = 'Нет'
        save_data()
    except Exception as e:
        print(f'worker_session Строка №39 - {e}')


# Функция добавления данных в БД что сотрудник начал смену
def append_start_session_on_data(worker_name):
    try:
        max_rw = SESSIONS_SHEET.max_row
        for i in range(max_rw+1):
            if SESSIONS_SHEET[f'A{i+1}'].value == None:
                SESSIONS_SHEET[f'A{i+1}'] = str(worker_name)
                SESSIONS_SHEET[f'B{i+1}'] = str(datetime.now())[:-7]
        save_data()
    except Exception as e:
        print(f'worker_session Строка №52 - {e}')


# Функция добавления данных в БД что сотрудник закончил смену
def append_end_session_on_data(worker_name):
    try:
        max_rw = SESSIONS_SHEET.max_row
        for i in range(max_rw + 1):
            if str(SESSIONS_SHEET[f'A{i+1}'].value) == str(worker_name) and SESSIONS_SHEET[f'C{i+1}'].value == None:
                SESSIONS_SHEET[f'C{i+1}'] = str(datetime.now())[:-7]
        save_data()
    except Exception as e:
        print(f'worker_session Строка №64 - {e}')


# В теории почти все функции выше, в этом файле, можно объеденить, но я писал их в самом начале
# А сейчас уже 36 день, как я делаю бота и мне лень это переписывать (:


# Функция для админа, просмотр смен сотрудников
def check_worker_session(worker_name, date):
    try:
        rtn_str = ''
        max_rw = SESSIONS_SHEET.max_row
        for i in range(max_rw + 1):
            if str(SESSIONS_SHEET[f'A{i+1}'].value) == str(worker_name) and str(SESSIONS_SHEET[f'B{i+1}'].value)[:-9] == str(date):
                rtn_str += f'{SESSIONS_SHEET[f"A{i+1}"].value}: {SESSIONS_SHEET[f"B{i+1}"].value}\n'
        return rtn_str
    except Exception as e:
        print(f'worker_session Строка №81 - {e}')


# Просмотр активных смен сотрудников
def check_active_sessions():
    try:
        rtn_str = ''
        max_rw_workers = WORKERS_SHEET.max_row
        for i in range(max_rw_workers):
            if str(WORKERS_SHEET[f'D{i+1}'].value) == 'Да':
                rtn_str += f'{WORKERS_SHEET[f"B{i+1}"].value}\n'
        return rtn_str
    except Exception as e:
        print(f'worker_session Строка №94 - {e}')