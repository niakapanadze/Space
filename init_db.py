from ext import app, db
from models import Planet


with app.app_context():
    db.drop_all()  # es dzval table-ebs shlis
    db.create_all()  # axlebit aketebs am table-s

    for planet in planets:
        new_planet = Planet(
            title=planet["title"],
            color=planet["color"],
            second_name=planet["second_name"],
            distance_million_km=planet["distance_million_km"],
            image=planet["img"],
            details=planet["details"]
        )
        db.session.add(new_planet)

    db.session.commit()  # samudamod inaxavs