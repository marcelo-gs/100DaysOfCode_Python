from flask import Flask, render_template, request, redirect, url_for
import sqlite3 
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float(), nullable=False)

    def __repr__(self):
        return '<Title %r>' % self.title



all_books = []
# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
# try:
#     cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# except sqlite3.OperationalError:
#     pass
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()


@app.route('/')
def home():
    all_books = db.session.query(Books).all()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == 'POST':
        new_book = Books(title=request.form['Bookname'], author=request.form['BookAuthon'],  rating=request.form['BookRating'])
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html")

@app.route("/edit", methods=["GET", "POST"])
def edit():
    book_to_update = Books.query.get(request.args.get('id'))
    print(request.args.get('id'), book_to_update)
    if request.method == 'POST':
        print(book_to_update)
        book_to_update.rating = request.form['BookRatingEdited']
        db.session.commit()  
        return redirect(url_for('home'))
    return render_template("edit.html", book=book_to_update)

@app.route("/delete", methods=["GET"])
def delete():
    book_to_delete = Books.query.get(request.args.get('id'))
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

