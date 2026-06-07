from ext import db, login_manager
from sqlalchemy import ForeignKey
from flask_login import UserMixin

class BaseModel:
    def create(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def save():
        db.session.commit()

class Planet(db.Model, BaseModel):
    __tablename__ = "planets"

    id = db.Column(db.Integer(), primary_key = True)
    title = db.Column(db.String(), nullable = False)
    color = db.Column(db.String(), nullable = False)
    second_name = db.Column(db.String(), nullable = False)
    distance_million_km = db.Column(db.Float(), nullable = False) # Float-it ar aris aucilebeli rom mteli ricxvi iyos. moon-ze maq 0.4
    image = db.Column(db.String(), default = "default.jpg")
    details = db.Column(db.String(), nullable = False)

class User(db.Model, BaseModel, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer(), primary_key = True)
    username = db.Column(db.String(), nullable = False, unique = True)
    age = db.Column(db.Integer())
    gender = db.Column(db.String())
    password = db.Column(db.String(), nullable = False)
    image = db.Column(db.String(), default = "pic.jpg")
    role = db.Column(db.String(), default = "Guest")

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Review(db.Model, BaseModel):
    __tablename__ = "reviews"

    id = db.Column(db.Integer(), primary_key = True)
    text = db.Column(db.String(), nullable = False)
    planet_id = db.Column(ForeignKey("planets.id"))