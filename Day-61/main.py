from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from flask_bootstrap import Bootstrap

class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(),Length(min=8)])
    submit = SubmitField(label="Log In")


def create_app():
  app = Flask(__name__)
  Bootstrap(app)

  return app

app = create_app()

app.secret_key = "okey-why-i-wil-secret-this"

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    email = "admin@email.com"
    password = "12345678"
    if login_form.validate_on_submit():
        # print(login_form.email.data)
        if login_form.email.data == email and login_form.password.data == password:
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template('login.html', form=login_form)



if __name__ == '__main__':
    app.run(debug=True)