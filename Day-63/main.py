from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
# import sqlite3

app = Flask(__name__)

# all_books = []
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db = SQLAlchemy(app)
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    #Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'
# with app.app_context():
#     db.create_all()
#     new_book = Book(
#         title = "Harry Potter",
#         author = "J. K. Rowling",
#         rating = 9.3
#     )
#     # db.session.add(new_book)
#     # db.session.commit()
#     # book = Book.query.filter_by(title="Harry Potter").first()
#     # book_to_update = Book.query.filter_by(title="Harry Potter").first()
#     # book_to_update.title = "Harry Potter and the Chamber of Secrets"
#     # db.session.commit()
#     book_id = 1
#     book_to_delete = Book.query.get(book_id)
#     db.session.delete(book_to_delete)
#     db.session.commit()


# print(book.author)

#Note: This All Code is for Squlite3. Here we use directly now we use another library to connect 

# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()
# cursor.execute("INSERT INTO books VALUES(2, 'Atomic Habit', 'James Clear', '9.8')")
# db.commit()
with app.app_context():
   # book = Book.query.filter_by(title="Harry Potter").first()
    all_books =  Book.query.all()
    print(all_books)



@app.route('/')
def home():
    return render_template("index.html", books = all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_bookX = {
            "title": request.form["name"],
            "author": request.form["author"],
            "rating": request.form["ratting"]
        }
        # all_books.append(new_book)
        with app.app_context():
            db.create_all()
            new_book = Book(
                title = request.form["name"],
                author = request.form["author"],
                rating =  float(request.form["ratting"])
            )
            db.session.add(new_book)
            db.session.commit()
            all_books =  Book.query.all()
        print(all_books)
        #NOTE: You can use the redirect method from flask to redirect to another route 
        # e.g. in this case to the home page after the form has been submitted.
        return redirect(url_for('home'))
    return render_template("add.html")
@app.route("/delete")
def delete():
    book_id = request.args.get('id')
    # book_id = num
    print(book_id)
    with app.app_context():
        book_to_delete = Book.query.get(book_id)
        db.session.delete(book_to_delete)
        db.session.commit()
    return redirect(url_for('home'))


@app.route("/edit", methods=["GET", "POST"])
def edit():
    book_id = request.args.get('id')
    with app.app_context():
        book = Book.query.filter_by(id=book_id).first()
    if request.method == "POST":
        new_rating = request.form["newRating"],
        print(new_rating)
        rating = float('.'.join(str(elem) for elem in new_rating))
        # rating = float(new_rating)
        print(rating)
        with app.app_context():
            book = Book.query.filter_by(id=book_id).first()
            book.rating = rating
            db.session.commit()
            all_books =  Book.query.all()
        return redirect(url_for('home'))

    # print(book)
    # book_to_update = Book.query.filter_by(title="Harry Potter").first()
    return render_template("edit.html", book = book)


if __name__ == "__main__":
    app.run(debug=True)

