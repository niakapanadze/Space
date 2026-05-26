from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, IntegerField, RadioField, SubmitField, SelectField
from wtforms.validators import DataRequired, EqualTo, Length
from flask_wtf.file import FileField, FileAllowed, FileSize


class RegisterForm(FlaskForm):
    username = StringField("Enter Username", validators=[DataRequired(), Length(min = 4, max = 20, message = "შენი სახელი უნდა იყოს 4 ასოდან 20 ასომდე, მეგობარო.")])
    age = IntegerField("Enter Age")
    gender = RadioField(choices = ["Female", "Male"])
    password = PasswordField("Enter Password", validators=[DataRequired(), Length(min = 8)])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('password', message = "არ ემთხვევა შენი ორი პაროლი, მეგობარო.")])
    image = FileField(
        "Upload Profile picture",
        validators = [
            FileAllowed(["jpg", "jpeg", "png"], "მხოლოდ ფოტოები შეიძლება, მეგობარო! ექსელის ფაილები და ეგეთი რაღაცეები არ მოსულა!"),
            FileSize(max_size = 5 * 1024 * 1024, message = "ფოტო უნდა იყოს 5 მეგაბიტზე ნაკლები, მეგობარო.")
        ]
    )
    register = SubmitField("Register")


class LoginForm(FlaskForm):
    username = StringField(
        "Enter Username",
        validators = [DataRequired()]
    )

    password = PasswordField(
        "Enter Password",
        validators = [DataRequired()]
    )
    login = SubmitField("Login")


class TravelForm(FlaskForm):
    planet = SelectField("Where do you want to go?(you are not going for real):", choices = [
        ("Mercury", "Mercury"),
        ("Venus", "Venus"),
        ("Earth", "Earth"),
        ("Mars", "Mars"),
        ("Jupiter", "Jupiter"),
        ("Saturn", "Saturn"),
        ("Uranus", "Uranus"),
        ("Neptune", "Neptune"),
        ("Pluto", "Pluto"),
        ("Sun", "Sun"),
        ("Moon", "Moon"),
        ("Black hole", "Black hole")
    ])

    vehicle = SelectField("Choose your vehicle:", choices = [
        ("airplane", "Airplane (900 km/h)"),
        ("rocket", "Apollo 11 Spacecraft (39,000 km/h)"),
        ("light", "Light (1,080,000,000 km/h)")
    ])
    submit = SubmitField("Calculate the time")