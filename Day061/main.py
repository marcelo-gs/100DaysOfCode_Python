from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap


def create_app():
  app = Flask(__name__)
  Bootstrap(app)
  app.secret_key= "secret"

  return app

app = create_app()

class MyForm(FlaskForm):
    email = StringField('E-Mail:', validators=[DataRequired(), Email()])
    password = PasswordField('Password:', 
                        validators=[DataRequired(), 
                        Length(4,8, "Field must be at least 8 characters long")])
    submit = SubmitField(label="Log In")
    #emailAdmin = "admin@email.com"
    #passwordAdmin = "12345678"
    

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    form = MyForm()
    if form.validate_on_submit():
        data_email = form.email.data
        data_password = form.password.data
        print(data_email, data_password)
        if "admin@email.com" == data_email and "12345678" == data_password:
            return render_template('success.html')
        else:
            return render_template('denied.html')
    print(form.errors)
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)