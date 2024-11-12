from flask import Flask, render_template


app = Flask(__name__)


@app.route("/numbers")
def numbers():
    return render_template("numbers.html", titel="Числа от 1 до 50")



if __name__ == '__main__':
    app.run()