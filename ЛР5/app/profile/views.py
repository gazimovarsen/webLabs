from .. import dbservice
from flask import render_template, flash, redirect, url_for, jsonify, request, Blueprint
# from .__init__ import profile

profile = Blueprint('profile', __name__)

links = [
        {'text': 'ГЛАВНАЯ', 'url': 'profile.index1'},
        {'text': 'О НАС', 'url': 'profile.index2'},
        {'text': 'ПРОЕКТЫ', 'url': 'profile.index2'},
        {'text': 'КОНТАКТЫ', 'url': 'profile.index3'}
    ]


@profile.route('/')
def index():
    # Redirect to the main index1 route
    return redirect(url_for('profile.index1'))


@profile.route('/index1/')
def index1():
    # url_for('static', filename='images/main-image-2.jpg')
    return render_template("index1.html", title='Главная', links=links, imgs=[url_for('static', filename='images/main-image-1.jpg'), url_for('static', filename='images/main-image-2.jpg')])


@profile.route('/index2/')
def index2():
    return render_template("index2.html", title='О нас', links=links)


@profile.route('/index3/', methods=['GET', 'POST'])
def index3():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        message2 = request.form['message2']
        return jsonify({'name': name, 'message': message, 'message2': message2})
    return render_template('index3.html', title='ФОРМА', links=links)


#-----------------------------------------------------------------------------------------------------------------------
@profile.route('/api/contactrequest', methods=['GET']) 
# Получаем все записи contactrequests из БД 
def get_contact_req_all(): 
    response = dbservice.get_contact_req_all() 
    return json_response(response) 


@profile.route('/api/contactrequest/<int:id>', methods=['GET']) 
# Получаем запись по id 
def get_contact_req_by_id(id): 
    response = dbservice.get_contact_req_by_id(id) 
    return json_response(response)


@profile.route('/api/contactrequest/author/<string:firstname>', methods=['GET']) 
# Получаем запись по имени пользователя 
def get_get_contact_req_by_author(firstname): 
    if not firstname: 
        # то возвращаем стандартный код 400 HTTP-протокола (неверный запрос) 
        return bad_request() 
    # Иначе отправляем json-ответ 
    else: 
        response = dbservice.get_contact_req_by_author(firstname) 
    return json_response(response)


@profile.route('/api/contactrequest', methods=['POST']) 
# Обработка запроса на создание новой записи в БД 
def create_contact_req(): 
    # Если в запросе нет данных или неверный заголовок запроса (т.е. нет 'application/json'), 
    # или в данных нет обязательного поля 'firstname' или 'reqtext' 
    if not request.json or not 'firstname' or not 'reqtext' in request.json: 
    # возвращаем стандартный код 400 HTTP-протокола (неверный запрос) 
        return bad_request() 
    # Иначе добавляем запись в БД отправляем json-ответ 
    else: 
        response = dbservice.create_contact_req(request.json) 
    return json_response(response)


