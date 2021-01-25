from flask import Flask, render_template, request, redirect, url_for
import sqlite3 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///marcelo2.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
# try:
#     cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# except sqlite3.OperationalError:
#     pass
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float(), nullable=False)

    def __repr__(self):
        return '<Title %r>' % self.title

db.create_all()
harrpypotter = Book(id=1, title="harry potter", author="J.K.", rating=9.4)
db.session.add(harrpypotter)
db.session.commit()

##Read All Records
all_books = db.session.query(Book).all()


#Read A Particular Record By Query
book = Book.query.filter_by(title="harry potter").first()


#Update A Particular Record By Query
book_to_update = Book.query.filter_by(title="harry potter").first()
book_to_update.title = "Harry Potter and the Chamber of Secrets"
db.session.commit()  


#Update A Record By PRIMARY KEY
book_id = 1
book_to_update = Book.query.get(book_id)
book_to_update.title = "Harry Potter and the Goblet of Fire"
db.session.commit()  


#Delete A Particular Record By PRIMARY KEY
book_id = 1
book_to_delete = Book.query.get(book_id)
db.session.delete(book_to_delete)
db.session.commit()
#You can also delete by querying for a particular value e.g. by title or one of the other properties.