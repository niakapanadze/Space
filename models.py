from ext import db

class Planet(db.Model):
    __tablename__ = "planets"

    id = db.Column(db.Integer(), primary_key = True)
    title = db.Column(db.String(), nullable = False)
    second_name = db.Column(db.String(), nullable = False)
    image = db.Column(db.String(), default = "default.jpg")