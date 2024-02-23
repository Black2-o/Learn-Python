import requests
from flask import Flask, render_template, request


app = Flask(__name__)

URL = "https://api.npoint.io/fbe2ee171668c89334d1"

response = requests.get(URL)
all_poast = response.json()

@app.route("/")
def get_all_posts():
    # print(all_poast)
    return render_template("index.html", posts=all_poast)

@app.route("/about")
def go_to_about():
    return render_template("about.html")

@app.route("/contact")
def go_to_contact():
    return render_template("contact.html")


@app.route("/contact", methods=["POST"])
def receive_data():
    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phn_number"]
    message = request.form["msghere"]
    print(f"{name}\n{email}\n{phone}\n{message}")
    return f"<h1>Sucessfully Send Your SMS</h1>"

## Send Email 

## This is not for now....


@app.route("/post/<num>")
def go_to_post(num):
    num = int(num)
    return render_template("post.html", no = num, posts=all_poast)











if __name__ == "__main__":
    app.run(debug=True)