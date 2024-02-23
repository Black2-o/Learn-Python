from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)

@app.route("/")
def home():
    random_number = random.randint(0, 100)    
    today = datetime.date.today()
    year = today.year

    return render_template("index.html", random_number=random_number, year = year)

@app.route("/username/<name>")
def name(name):
    GENDER_API = f"https://api.genderize.io?name={name}"
    GENERAL_API = f"https://api.agify.io/?name={name}"

    response1 = requests.get(GENDER_API)
    response2 = requests.get(GENERAL_API)
    age_data = response2.text
    age = age_data.split('"age":')[1].split("}")[0]

    gender_data = response1.text
    gender = gender_data.split('"gender":"')[1].split('",')[0]
    return render_template("name.html", name = name, gender = gender, age = age)



@app.route("/blog/<num>")
def get_blog(num):
    blog_url = "https://api.npoint.io/bd948ffae277f4777aab"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts= all_posts)


if __name__ == "__main__":
    app.run(debug=True)


