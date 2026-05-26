from ext import db

class Planet(db.Model):
    __tablename__ = "planets"

    id = db.Column(db.Integer(), primary_key = True)
    title = db.Column(db.String(), nullable = False)
    color = db.Column(db.String(), nullable = False)
    second_name = db.Column(db.String(), nullable = False)
    distance_million_km = db.Column(db.Float(), nullable = False) # Float-it ar aris aucilebeli rom mteli ricxvi iyos. moon-ze maq 0.4
    image = db.Column(db.String(), default = "default.jpg")
    details = db.Column(db.String(), nullable = False)

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer(), primary_key = True)
    username = db.Column(db.String(), nullable = False, unique = True)
    age = db.Column(db.Integer())
    gender = db.Column(db.String())
    password = db.Column(db.String(), nullable = False)
    image = db.Column(db.String(), default = "pic.jpg")