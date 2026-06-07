from models import Planet, User, Review
from ext import app, db
from forms import RegisterForm, LoginForm, TravelForm, PlanetForm
from flask import Flask, render_template, redirect, flash
from flask_login import login_user, logout_user, login_required
from os import path


@app.route("/")
def home():
    planets = Planet.query.all()
    return render_template("index.html", planets = planets, role = "admin") # HTML-ისთვის ცვლადის გადაცემა


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            flash(f"Login successful for {user.username}!")
            return redirect("/")
        else:
            flash("No such user or the password is incorrect!")
    return render_template("login.html", form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/profile/<int:profile_id>") # profile_id დინამიური ცვლადია, რომელიც int ტიპია (int:) ამ შემთხვევაში. default-ად სტრინგია
def profile(profile_id):
    if profile_id < len(profiles):
        profile = profiles[profile_id]
        return render_template("profile.html", profile=profile)
    return "Profile not found"
    return render_template("profile.html", profile=profile)


@app.route("/planet/<int:planet_id>")
def view_planet_details(planet_id):
    planet = Planet.query.get(planet_id)
    if planet:
        reviews = Review.query.filter(Review.planet_id == planet_id).all()
        return render_template("planet_details.html",
                               planet=planet,
                               reviews=reviews)
    return "Planet Not Found"

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        img_file = form.image.data
        filename = "pic.jpg"

        if img_file:
            filename = img_file.filename
            directory = path.join(app.root_path, "static", "images", filename)
            img_file.save(directory)

        # user=shi aseivebs
        new_user = User(
            username = form.username.data,
            age = form.age.data,
            gender = form.gender.data,
            password = form.password.data,
            image = filename
        )

        # db.session.add(new_user) db.session.commit() --- igivea rac:
        new_user.create()

        flash(f"User {form.username.data} has been successfully saved to the database!")
        return redirect("/")

    return render_template("register.html", form=form)

@app.route("/travel", methods=["GET", "POST"])
def travel_simulator():
    form = TravelForm()
    result = None

    if form.validate_on_submit():
        selected_planet = form.planet.data
        selected_vehicle = form.vehicle.data

        # aq edzebs distance-s
        planet = Planet.query.filter(Planet.title == selected_planet).first()

        if planet:
            distance = planet.distance_million_km * 1000000

            if selected_vehicle == "airplane":
                speed = 900
            elif selected_vehicle == "rocket":
                speed = 39000
            else:
                speed = 1080000000

            hours = distance / speed
            days = hours / 24
            years = days / 365

            if years > 1:
                result = f"It would take about {round(years, 1)} years to reach {selected_planet}! But you are not gonna go there anyway!"
            elif days > 1:
                result = f"It would take about {round(days, 1)} days to reach {selected_planet}! But you are not gonna go there anyway!"
            else:
                result = f"It would take about {round(hours, 1)} hours to reach {selected_planet}! But you are not gonna go there anyway!"

    return render_template("travel.html", form=form, result = result)


@app.route("/add_planet", methods=["GET", "POST"])
@login_required
def add_planet():
    form = PlanetForm()
    # tu gilaks daawira
    if form.validate_on_submit():
        new_planet = Planet(
            title = form.title.data,
            color = form.color.data,
            second_name = form.second_name.data,
            distance_million_km = form.distance_million_km.data,
            details = form.details.data
        )

        img = form.image.data
        if img:
            new_planet.image = img.filename
            directory = path.join(app.root_path, "static", "images", img.filename)
            img.save(directory)

        # es database-shi aseivebs
        #db.session.add(new_planet) db.session.commit() --- givea raas:
        new_planet.create()
        flash("Your planet has been successfully added!")
        return redirect("/")

    return render_template("add_planet.html", form=form)


@app.route("/update_planet/<int:planet_id>", methods=["GET", "POST"])
@login_required
def update_planet(planet_id):
    # aq vedzebt planetas romlis shcvlac gvindaaaa
    planet = Planet.query.get(planet_id)

    # aq ukve unda eweros tavidan rac ewera rom mere shevcvalot
    form = PlanetForm(
        title=planet.title,
        color=planet.color,
        second_name=planet.second_name,
        distance_million_km=planet.distance_million_km,
        details=planet.details
    )

    if form.validate_on_submit():
        # aq dzvels cvlis axlit
        planet.title = form.title.data
        planet.color = form.color.data
        planet.second_name = form.second_name.data
        planet.distance_million_km = form.distance_million_km.data
        planet.details = form.details.data

        image = form.image.data
        if image:
            directory = path.join(app.root_path, "static", "images", image.filename)
            image.save(directory)
            planet.image = image.filename

        planet.save()  # aseivebs rac shevcvalet imas
        return redirect("/")

    return render_template("add_planet.html", form=form)


@app.route("/delete_planet/<int:planet_id>")
@login_required
def delete_planet(planet_id):
    # vedzebt planets id-it
    planet = Planet.query.get(planet_id)

    # vashorebt da mere vaseivebt cvlilebebs
    # db.session.delete(planet) db.session.commit() --- igivea rac:
    planet.delete()
    return redirect("/")