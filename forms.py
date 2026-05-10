from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, IntegerField, RadioField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length
from flask_wtf.file import FileField


class RegisterForm(FlaskForm):
    username = StringField("Enter Username", validators=[DataRequired(), Length(min = 4, max = 20)])
    age = IntegerField("Enter Age")
    gender = RadioField(choices = ["Female", "Male"])
    password = PasswordField("Enter Password", validators=[DataRequired(), Length(min = 8)])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('password')])
    image = FileField("Upload Profile Picture")
    register = SubmitField("Register")


class LoginForm(FlaskForm):
    username = StringField("Enter Username")
    password = PasswordField("Enter Password")

    login = SubmitField("Login")