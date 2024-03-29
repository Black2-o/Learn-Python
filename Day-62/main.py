from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, RadioField
from wtforms.validators import DataRequired
import csv


def create_app():
  app = Flask(__name__)
  Bootstrap(app)

  return app

app = create_app()

app.secret_key = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Cafe Location on Google Maps (URL)', validators=[DataRequired()])
    openN = StringField('Opening Time e.g. 8AM', validators=[DataRequired()])
    close = StringField('Closing Time e.g. 5.30 PM', validators=[DataRequired()])
    coffee = SelectField(u'Coffee Rating name', choices=[('☕'), ('☕☕'), ('☕☕☕'),('☕☕☕☕'), ('☕☕☕☕☕')])
    wifi = SelectField(u'Wifi Strength Rating', choices=[('✘'), ('💪'), ('💪💪'), ('💪💪💪'),('💪💪💪💪'), ('💪💪💪💪💪')])
    power = SelectField(u'Power Socket Availability', choices=[('✘'), ('🔌'), ('🔌🔌'), ('🔌🔌🔌'),('🔌🔌🔌🔌'), ('🔌🔌🔌🔌🔌')])
    submit = SubmitField(label='Submit')

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


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()

    if form.validate_on_submit():
            print("True")
            cafeX = form.cafe.data
            locationX = form.location.data
            openNX = form.openN.data
            closeX = form.close.data
            coffeeX = form.coffee.data
            wifiX = form.wifi.data
            powerX = form.power.data
            with open("cafe-data.csv", "a", encoding="utf-8") as file:
                file.write(f"\n{cafeX},{locationX},{openNX},{closeX},{coffeeX},{wifiX},{powerX}")
            return cafes()
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding="utf8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        # print(csv_data)
        for row in csv_data:
            list_of_rows.append(row)
        # print(list_of_rows)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
