from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World'

@app.route('/<x>/<y>/add')
def add(x, y):
    x, y = float(x), float(y)
    return f'{x} + {y} = {x + y}'

@app.route('/<x>/<y>/sub')
def sub(x, y):
    x, y = float(x), float(y)
    return f'{x} - {y} = {x - y}'

@app.route('/<x>/<y>/multi')
def multi(x, y):
    x, y = float(x), float(y)
    return f'{x} * {y} = {x * y}'

@app.route('/<x>/<y>/split')
def split(x, y):
    x, y = float(x), float(y)
    if y:
        return f'{x} / {y} = {x / y}'
    else:
        return "Недопустимое действие, делить на ноль нельзя"

@app.route('/hello')
def hello_world():
    name = request.args.get('name', 'World')
    surname = request.args.get('surname', 'User')
    return f'Hello {name} {surname}!'

def get_all_users_form_db():
    return [
        {
            "id": 1,
            "username": "Alice",
            "email": "alice@mail.ru"
        },
        {
            "id": 23,
            "username": "Boris",
            "email": "boris@yandex.ru"
        }
    ]

@app.route('/users')
def get_users():
    users = []
    for user in get_all_users_form_db():
        users.append(user)
    return jsonify(users)


if __name__ == '__main__':
    app.run()


#Задание
#Создайте страницу сайта, которая будет доступна по данному URL(http://127.0.0.1:5000/NUMBER_ONE/NUMBER_TWO/OPEATION), где
#NUMBER_ONE, NUMBER_TWO - числа, которые передают в виде параметра
#OPERATION - арифметическая операция между числами
#(сложение, вычитание, умножение и деление первого числа на второго с дробной частью, если это сделать невозможно, нужно вывести соответствующее сообщение).