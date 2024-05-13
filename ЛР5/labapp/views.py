from labapp import app
from . import dbservice
from flask import render_template, make_response, request, Response, jsonify, json, url_for, session, redirect
import functools

links = [
        {'text': 'ГЛАВНАЯ', 'url': 'index1'},
        {'text': 'О НАС', 'url': 'index2'},
        {'text': 'ПРОЕКТЫ', 'url': 'index2'},
        {'text': 'КОНТАКТЫ', 'url': 'index3'}
    ]


@app.route('/register', methods=['GET', 'POST']) 
def register(): 
    # Если POST-запрос, регистрируем нового пользователя 
    if request.method == 'POST': 
        return dbservice.register_user(request.form) 
    else: 
        return render_template('register.html', title='Register')


@app.route('/')
@app.route('/index1/')
def index1():
    # url_for('static', filename='images/main-image-2.jpg')
    return render_template("index1.html", title='Главная', links=links, imgs=[url_for('static', filename='images/main-image-1.jpg'), url_for('static', filename='images/main-image-2.jpg')])


@app.route('/index2/')
def index2():
    return render_template("index2.html", title='О нас', links=links)

@app.route('/index3/')
def index3():
    return render_template('index3.html', title='ФОРМА', links=links)


def login_required(route_func): 
    @functools.wraps(route_func) 
    def decorated_route(*args, **kwargs): 
    # Если не установлен параметр сессии user или значение cookie 'AuthToken' не равно логину пользователя 
        if not session.get('user') or request.cookies.get('AuthToken') != session.get('user'): 
        # перенаправляем на страницу авторизации 
            return redirect(url_for('login')) 
        return route_func(*args, **kwargs) 
    return decorated_route


@app.route('/contact') 
@login_required 
def contact(): 
    return render_template('index3.html', title='НУ ВОТ ТАК')


@app.route('/login', methods=['GET', 'POST'])
def login():
    # Если POST-запрос
    if request.method == 'POST':
        # если нажата кнопка "Зарегистрировать", переадресуем на страницу регистрации
        if request.form.get('regBtn') == 'true':
            return redirect(url_for('register'))
        # иначе запускаем авторизацию по данным формы
        else:
            return dbservice.login_user(request.form)
    else:
        return render_template('login.html', title='LOGIN')


#-----------------------------------------------------------------------------------------------------------------------
@app.route('/api/contactrequest', methods=['GET']) 
# Получаем все записи contactrequests из БД 
def get_contact_req_all(): 
    response = dbservice.get_contact_req_all() 
    return json_response(response) 


@app.route('/api/contactrequest/<int:id>', methods=['GET']) 
# Получаем запись по id 
def get_contact_req_by_id(id): 
    response = dbservice.get_contact_req_by_id(id) 
    return json_response(response)


@app.route('/api/contactrequest/author/<string:firstname>', methods=['GET']) 
# Получаем запись по имени пользователя 
def get_get_contact_req_by_author(firstname): 
    if not firstname: 
        # то возвращаем стандартный код 400 HTTP-протокола (неверный запрос) 
        return bad_request() 
    # Иначе отправляем json-ответ 
    else: 
        response = dbservice.get_contact_req_by_author(firstname) 
    return json_response(response)


@app.route('/api/contactrequest', methods=['POST']) 
# Обработка запроса на создание новой записи в БД 
def create_contact_req(): 
    # Если в запросе нет данных или неверный заголовок запроса (т.е. нет 'application/json'), 
    # или в данных нет обязательного поля 'firstname' или 'reqtext' 
    if not request.json or not 'firstname' or not 'first_message' in request.json:
        print("gepa")
        return bad_request() 
    # Иначе добавляем запись в БД отправляем json-ответ 
    else: 
        response = dbservice.create_contact_req(request.json) 
    return json_response(response)

@app.route('/api/contactrequest/<int:id>', methods=['PUT'])
# Обработка запроса на обновление записи в БД
def update_contact_req_by_id(id):
    # Если в запросе нет данных или неверный заголовок запроса (т.е. нет 'application/json'),
    # или в данных нет обязательного поля 'reqtext'
    if not request.json or not 'first_message' in request.json:
        # возвращаем стандартный код 400 HTTP-протокола (неверный запрос)
        return bad_request()
    # Иначе обновляем запись в БД и отправляем json-ответ
    else:
        response = dbservice.update_contact_req_by_id(id, request.json)
        return json_response(response)


@app.route('/api/contactrequest/<int:id>', methods=['DELETE'])
# Обработка запроса на удаление записи в БД по id
def delete_contact_req_by_id(id):
    response = dbservice.delete_contact_req_by_id(id)
    return json_response(response)

"""
    Реализация response-методов, возвращающих клиенту стандартные коды протокола HTTP
"""


# Возврат html-страницы с кодом 404 (Не найдено)
@app.route('/notfound')
def not_found_html():
    return render_template('404.html', title='404', err={ 'error': 'Not found', 'code': 404 })


# Формирование json-ответа. Если в метод передается только data (dict-объект), то по-умолчанию устанавливаем код возврата code = 200
# В Flask есть встроенный метод jsonify(dict), который также реализует данный метод (см. пример метода not_found())
def json_response(data, code=200):
    return Response(status=code, mimetype="application/json", response=json.dumps(data))


# Пример формирования json-ответа с использованием встроенного метода jsonify()
# Обработка ошибки 404 протокола HTTP (Данные/страница не найдены)
def not_found():
    return make_response(jsonify({'error': 'Not found'}), 404)


# Обработка ошибки 400 протокола HTTP (Неверный запрос)
def bad_request():
    return make_response(jsonify({'error': 'Bad request'}), 400)
