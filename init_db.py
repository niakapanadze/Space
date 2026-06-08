from ext import app, db
from models import Planet, User

with app.app_context():
    # db.drop_all()  # წაშალე ყველა ცხრილი რაც კი ბაზაში არის
    db.create_all()  # შექმენი ყველა ცხრილი რაც დაიმპორტებულია

    admin = User(username = "admin",
                 password = "adminpass",
                 role = "Admin")
    admin.create()