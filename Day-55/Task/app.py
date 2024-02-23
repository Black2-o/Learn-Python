from flask import Flask
import random

app = Flask(__name__)


def make_bold(function):
    def wrapper_function():
        return "<b>" + function() + "</b>"
    return wrapper_function

def make_italic(function):
    def wrapper():
        return "<i>" + function() + "</i>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper


@app.route("/")
def hello_world():
    return '<h1 style="text-align:center;">Hello World</h1>'\
        '<p style="text-align:center;">This is Pragraph.</p>'\
            '<img src="https://media.giphy.com/media/CY9jl58dVtU2s/giphy.gif" width=200>'


@app.route("/bye")
@make_bold
@make_italic
@make_underlined
def say_bye():
    return "Good Bye"

@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello {name}! You are {number} years old!"



if __name__ == "__main__":
    app.run(debug=True)
