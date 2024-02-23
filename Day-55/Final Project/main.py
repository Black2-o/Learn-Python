from flask import Flask
import random

app = Flask(__name__)

MAIN_GIF = "https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"
HIGH = "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"
LOW = "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"
CORRECT = "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"
RANDOM_NUMBER = random.randint(0, 9)


@app.route("/")
def hello_world():
    return '<h1 style="text-align:center;">Guess a number between 0 and 9</h1>'\
        f'<img src="{MAIN_GIF}"/>'

@app.route("/<int:number>")
def greet(number):
    if number == RANDOM_NUMBER:
        return "<h1 style='text-align:center; color:green'>YOU FOUND ME</h1>"\
            f"<img src='{CORRECT}'/>"
    elif number > RANDOM_NUMBER:
        return "<h1 style='text-align:center; color:purple'>TOO HIGH, TRY AGAIN</h1>"\
            f"<img src='{HIGH}'/>"
    elif number < RANDOM_NUMBER:
        return "<h1 style='text-align:center; color:red'>TOO LOW, TRY AGAIN</h1>"\
            f"<img src='{LOW}'/>"



if __name__ == "__main__":
    app.run(debug=True)
