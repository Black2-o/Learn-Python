import requests
from flask import Flask, render_template


app = Flask(__name__)

URL = "https://api.npoint.io/fbe2ee171668c89334d1"

# response = requests.get(URL)
# all_poast = response.json()


@app.route("/")
def get_all_posts():
    print(all_poast)
    return render_template("index.html", posts=all_poast)


@app.route("/about")
def go_to_about():
    return render_template("about.html")


@app.route("/contact")
def go_to_contact():
    return render_template("contact.html")


@app.route("/post/<num>")
def go_to_post(num):
    num = int(num)
    return render_template("post.html", no=num, posts=all_poast)


if __name__ == "__main__":
    app.run(debug=True)
