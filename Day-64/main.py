from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests
from sqlalchemy.orm import DeclarativeBase


class EditForm(FlaskForm):
    up_rating = FloatField(
        label='Your Rating Out 10 e.g.. 7.5', validators=[DataRequired()])
    up_review = StringField(label='Your Review', validators=[DataRequired()])
    submit = SubmitField(label="Done")


class AddNew(FlaskForm):
    name = StringField(label='Movie Title', validators=[DataRequired()])
    submit = SubmitField(label="Add Movie")


MOVIE_DB_API_KEY = '78f7769b5b55a9b114c957e896330090'
MOVIE_DB_SEARCH_URL = 'https://api.themoviedb.org/3/search/movie?'

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
db = SQLAlchemy(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'


# with app.app_context():
#     db.create_all()


with app.app_context():
    new_movie = Movie(
        title="Phone Booth",
        year=2002,
        description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
        rating=7.3,
        ranking=10,
        review="My favourite character was the caller.",
        img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
    )

    # db.session.add(new_movie)
    # db.session.commit()


# Open Database
with app.app_context():
    movie_list = Movie.query.all()


@app.route("/")
def home():
    return render_template("index.html", movies=movie_list)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    edit_form = EditForm()
    movie_id = request.args.get('id')
    print(movie_id)
    movie = Movie.query.filter_by(id=movie_id).first()
    if edit_form.validate_on_submit():
        # print(movie)
        movie.rating = edit_form.up_rating.data
        movie.review = edit_form.up_review.data
        db.session.commit()
        movie_list = Movie.query.all()
        return redirect(url_for('home'))
    return render_template("edit.html", form=edit_form)


@app.route("/delete", methods=["GET", "POST"])
def delete():
    movie_id = request.args.get('id')
    print(movie_id)
    movie_to_delete = Movie.query.filter_by(id=movie_id).first()
    print(movie_to_delete)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/add", methods=["GET", "POST"])
def add():
    new_movieX = AddNew()
    if new_movieX.validate_on_submit():
        response = requests.get(MOVIE_DB_SEARCH_URL, params={
            "api_key": MOVIE_DB_API_KEY, "query": new_movieX.name.data})
        data = response.json()["results"]
        return render_template("select.html", movie=data)
    return render_template('add.html', movie=new_movieX)


@app.route("/final_add", methods=["GET", "POST"])
def final_add():
    movie_api_id = request.args.get('id')
    if movie_api_id:
        url = f"https://api.themoviedb.org/3/movie/{movie_api_id}"
        # movie_api_url = f"{MOVIE_DB_SEARCH_URL}/{movie_api_id}"
        # The language parameter is optional, if you were making the website for a different audience
        # e.g. Hindi speakers then you might choose "hi-IN"
        response = requests.get(url, params={
                                "api_key": MOVIE_DB_API_KEY, "language": "en-US"})
        data = response.json()
    # print(data)
    with app.app_context():
        new_movie = Movie(
            title=data["original_title"],
            # The data in release_date includes month and day, we will want to get rid of.
            year=data["release_date"][0:4],
            img_url="https://image.tmdb.org/t/p/w500/" + data["poster_path"],
            description=data["overview"]
        )
        print(new_movie)
        db.session.add(new_movie)
        db.session.commit()
    return redirect(url_for('edit'))


if __name__ == '__main__':
    app.run(debug=True)
