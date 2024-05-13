from labapp import db
from datetime import datetime
from sqlalchemy.sql import text
from collections import OrderedDict

"""
    В данном модуле реализуются CRUD-методы для работы с БД.
    Если в вашем приложении используется несколько сущностей (таблиц) в БД, то хорошей практикой 
    будет являться реализация ОТДЕЛЬНЫХ модулей с CRUD-операциями для каждой таблицы, при этом 
    данные модули лучше группировать в отдельном пакете Python, т.е. создавать папку с файлом __init__.py
"""
columns = ["id", "firstname", "first_message", "second_message", "createdAt", "updatedAt"]

# Получаем список всех запросов.
def get_contact_req_all():
    result = []     # создаем пустой список
    # Получаем итерируемый объект, где содержатся все строки таблицы contactrequests
    rows = db.session.execute(text("SELECT * FROM contactrequests")).fetchall()
    # Каждую строку конвертируем в стандартный dict, который Flask может трансформировать в json-строку
    # for row in rows:
    #     result.append(dict(row))

    for row in rows:
        d = OrderedDict()
        arr = zip(columns, row)
        for col, el in arr:
            d[col] = el
            print(el)
        result.append(d)    
    # возвращаем dict, где result - это список с dict-объектов с информацией
    return {'contactrequests': result}


# Получаем запрос с фильтром по id
def get_contact_req_by_id(id):
    result = db.session.execute(text(f"SELECT * FROM contactrequests WHERE id = {id}")).fetchone()
    d = OrderedDict()
    arr = zip(columns, result)
    for col, el in arr:
        d[col] = el
        print(el)
    return d


# Получаем все запросы по имени автора
def get_contact_req_by_author(firstname):
    result = []
    rows = db.session.execute(text(f"SELECT * FROM contactrequests WHERE firstname = '{firstname}'")).fetchall()
    for row in rows:
        d = OrderedDict()
        arr = zip(columns, row)
        for col, el in arr:
            d[col] = el
            print(el)
        result.append(d)
    return {'contactrequests': result}


# Создать новый запрос
def create_contact_req(json_data):
    try:
        cur_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")     # текущая дата и время
        # INSERT запрос в БД
        print(json_data)
        db.session.execute(text(f"INSERT INTO contactrequests "
                           f"(firstname, first_message, second_message, cratedAt, updatedAt) "
                           f"VALUES ("
                           f"'{json_data['firstname']}', "
                           f"'{json_data['first_message']}', "
                           f"'{json_data['second_message']}', "
                           f"'{cur_time}', "
                           f"'{cur_time}')"
        ))
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1")
        # Подтверждение изменений в БД
        db.session.commit()
        # Возвращаем результат
        
        print(json_data['firstname'])
        return {'message': "ContactRequest Created!"}
        # если возникла ошибка запроса в БД
    except Exception as e:
        # откатываем изменения в БД
        db.session.rollback()
        # возвращаем dict с ключом 'error' и текcтом ошибки
        return {'message': str(e)}


# Удалить запрос по id в таблице
def delete_contact_req_by_id(id):
    try:
        # DELETE запрос в БД
        db.session.execute(text(f"DELETE FROM contactrequests WHERE id = {id}"))
        db.session.commit()
        return {'message': "ContactRequest Deleted!"}
    except Exception as e:
        db.session.rollback()
        return {'message': str(e)}


# Обновить текст запроса по id в таблице
def update_contact_req_by_id(id, json_data):
    try:
        cur_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # текущая дата и время
        # UPDATE запрос в БД
        db.session.execute(text(f"UPDATE contactrequests SET first_message = '{json_data['first_message']}', "
                           f"updatedAt = '{cur_time}' WHERE id = {id}"))
        db.session.commit()
        return {'message': "ContactRequest Updated!"}
    except Exception as e:
        db.session.rollback()
        return {'message': str(e)}
