from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, Length
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

Bootstrap(app)
db = SQLAlchemy(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return '<Title %r>' % self.title

db.create_all()

# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
# db.session.add(new_movie)
# db.session.commit()

class RateMovieForm(FlaskForm):
    rating = FloatField('Rating:', validators=[DataRequired()])
    review = StringField('Review:', validators=[DataRequired(), Length(4,250, "Field must be at least 250 characters long")])
    submit = SubmitField(label="Done")

class AddMovie(FlaskForm):
    title = StringField('Title:', validators=[DataRequired(), Length(4,250, "Field must be at least 250 characters long")])
    submit = SubmitField(label="Search")

@app.route("/", methods=["GET"])
def home():
    all_movies = Movie.query.order_by(Movie.rating, Movie.title).all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = RateMovieForm()
    movie = Movie.query.get(request.args.get('id'))
    if form.validate_on_submit():
        movie.rating = request.form['rating']
        movie.review = request.form['review']
        db.session.commit() 
        return redirect(url_for('home'))
    return render_template("edit.html", form=form)

@app.route("/delete", methods=["GET"])
def delete():
    movie = Movie.query.get(request.args.get('id'))
    db.session.delete(movie)
    db.session.commit() 
    return redirect(url_for('home'))

@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddMovie()
    if form.validate_on_submit():
        url = "https://api.themoviedb.org/3/search/movie"
        params = {
            "api_key": "1e08d58343e2f8e9c7a60751e4329d46",
            "language":"en-US",
            "query":request.form['title'],
            "page":1,
            "include_adult":"true"
        }
        data = requests.get(url=url, params=params).json()['results']
        return render_template("select.html", movies=data)
    return render_template("add.html", form=form)

@app.route("/select", methods=["GET"])
def select():
    movie_id = request.args.get('id')
    url = "https://api.themoviedb.org/3/movie/" + movie_id
    params = {
            "api_key": "1e08d58343e2f8e9c7a60751e4329d46",
            "language":"en-US"
        }
    data = requests.get(url=url, params=params).json()
    movie = Movie(title=data['title'], 
                    year = data['release_date'][:4], 
                    description = str(data['tagline'] + "\n" + data['overview'])[:250],
                    rating = 0,
                    ranking = 0, 
                    review = "", 
                    img_url = "https://image.tmdb.org/t/p/w500" + data['poster_path'])
    db.session.add(movie)
    db.session.commit()
    return redirect(url_for('edit', id=movie.id))

if __name__ == '__main__':
    app.run(debug=True)
