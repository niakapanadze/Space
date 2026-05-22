from ext import app, db
from models import Planet

with app.app_context():
    db.drop_all()
    db.create_all()