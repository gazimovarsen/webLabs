from . import profile
from flask import render_template, flash, redirect, url_for, jsonify, request

links = [
        {'text': 'ГЛАВНАЯ', 'url': 'profile.index1'},
        {'text': 'О НАС', 'url': 'profile.index2'},
        {'text': 'ПРОЕКТЫ', 'url': 'profile.index2'},
        {'text': 'КОНТАКТЫ', 'url': 'profile.index3'}
    ]


@profile.route('/')
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
