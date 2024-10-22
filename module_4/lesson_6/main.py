from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, world!"


@app.route('/info')
def information():
    return "Сегодня хорошая погода!"


@app.route('/world')
def world():
    return """
Природа Ростовской области, несмотря на расположение области на юге страны, разнообразна. 
Это подтверждает и то, что на территории области находится множество охраняемых природных зон: биосферный заповедник, природные заказчики и парки, памятники природы.
"""


if __name__ == '__main__':
    app.run()
    