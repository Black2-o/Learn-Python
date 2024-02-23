from flask import Flask, render_template
import requests

app = Flask(__name__)

blog_url = "https://api.npoint.io/bd948ffae277f4777aab"
response = requests.get(blog_url)
all_posts = response.json()
# print(all_posts)

@app.route('/')
def home():
    return render_template("index.html")


@app.route("/blog")
def blog():
    return render_template("index.html", posts= all_posts)
@app.route("/blog/<num>")
def posts(num):
    numInt = int(num)
    return render_template("post.html", posts= all_posts, num=numInt)


if __name__ == "__main__":
    app.run(debug=True)
