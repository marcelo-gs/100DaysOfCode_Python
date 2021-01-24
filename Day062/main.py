from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class AddCafeForm(FlaskForm):
    coffee_choise = ["☕"*(i+1) for i in range(5)]
    wifi_choise = ["✘", "💪","💪💪",'💪💪💪', '💪💪💪💪', "💪💪💪💪💪"]
    power_choise = ["✘", '🔌', "🔌🔌", '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌']
    
    cafe_name = StringField('Cafe Name:', validators=[DataRequired()])
    cafe_location = StringField('Cafe Location on Google Maps (URL):', 
                        validators=[DataRequired()])
    cafe_open_time = StringField('Open Time e.g (8AM):', validators=[DataRequired()])
    cafe_close_time = StringField('Close Time e.g (10PM):', validators=[DataRequired()])
    cafe_coffee_rating = SelectField('Coffee Rating:', validators=[DataRequired()], choices=coffee_choise)
    cafe_wifi_strong_rating = SelectField('WiFi Strong Rating:', validators=[DataRequired()], choices=wifi_choise)
    cafe_power_socket_avaliable = SelectField('Power Socket Avaliable:', validators=[DataRequired()], choices=power_choise)
    submit = SubmitField(label="Add Cafe")

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = AddCafeForm()
    if form.validate_on_submit():
        print("True")
        cafe_name = form.cafe_name.data
        cafe_location  = form.cafe_location.data
        cafe_open_time = form.cafe_open_time.data
        cafe_close_time = form.cafe_close_time.data
        cafe_coffee_rating = form.cafe_coffee_rating.data
        cafe_wifi_strong_rating = form.cafe_wifi_strong_rating.data
        cafe_power_socket_avaliable = form.cafe_power_socket_avaliable.data
        write_line_in_csv(cafe_name, cafe_location, cafe_open_time, cafe_close_time, 
        cafe_coffee_rating, cafe_wifi_strong_rating, cafe_power_socket_avaliable)
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


def write_line_in_csv(cafe_name, cafe_location, cafe_open_time, cafe_close_time, 
        cafe_coffee_rating, cafe_wifi_strong_rating, cafe_power_socket_avaliable):
    line = cafe_name + ',' + cafe_location + ","+ cafe_open_time + "," + cafe_close_time + "," + cafe_coffee_rating + "," + cafe_wifi_strong_rating + "," + cafe_power_socket_avaliable + "\n"
    with open('cafe-data.csv', encoding="utf-8", mode="a") as csv_file:
        csv_file.write(line)




@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding="utf-8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows[1:])


if __name__ == '__main__':
     app.run(debug=True)
