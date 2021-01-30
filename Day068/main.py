from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = "static/files"

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
#Line below only required once, when creating DB. 
# db.create_all()


@app.route('/')
def home():
    # Every render_template has a logged_in variable set.
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=["GET", "POST"])
def register():

    if request.method == 'POST':

        if User.query.filter_by(email=request.form.get('email')).first():
            #User already exists
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('login'))

        # new_user = User()
        # new_user.email = request.form['email']
        # new_user.password = request.form['password']
        # new_user.name = request.form['name']

        password = generate_password_hash(request.form.get('password'), "pbkdf2:sha256", 8)
        print(password)
        new_user = User(
            email=request.form.get('email'),
            name=request.form.get('name'),
            password=password
        )
        db.session.add(new_user)
        db.session.commit()

        #Log in and authenticate user after adding details to database.
        login_user(new_user)

        return redirect(url_for('secrets', username=new_user.name))
    return render_template("register.html", logged_in=current_user.is_authenticated)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        
        #Find user by email entered.
        user = User.query.filter_by(email=email).first()
        
        #Email doesn't exist
        if not user:
            flash("That email does not exist, please try again.")
            return redirect(url_for('login'))
        #Password incorrect
        elif not check_password_hash(user.password, password):
            flash('Password incorrect, please try again.')
            return redirect(url_for('login'))
        #Email exists and password correct
        else:
            login_user(user)
            return redirect(url_for('secrets'))
                  
    return render_template("login.html", logged_in=current_user.is_authenticated)



@app.route('/secrets')
@login_required
def secrets():
    username = request.args.get("username")
    return render_template("secrets.html", username=username, logged_in=True)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/download')
@login_required
def download():
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               "cheat_sheet.pdf", as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)