import os
import requests
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")
API_KEY = os.environ.get("API_KEY")

mongo = PyMongo(app)

@app.route("/")
@app.route("/get_games")
def get_games():
    '''Home page, gets 15 results from rawg API and uses Jinja to display each'''
    parameters = {
        "page_size": 12
    }
    response = requests.get(f"https://api.rawg.io/api/games?key={API_KEY}", params=parameters)
    data = response.json()


    return render_template("games.html", data=data)



@app.route("/")
@app.route("/get_reviews")
def get_tasks():
    '''Shows list of reviews from Mongodb'''
    reviews = mongo.db.reviews.find()
    return render_template("reviews.html", reviews=reviews)


@app.route("/register", methods=["GET", "POST"])
def register():
    '''Checks if password matches, if it does registers new user if they dont already exist'''
    if request.form.get("password") == request.form.get("confirm-password"):
        #check if password matches
        if request.method == "POST":
            #check if username exists
            existing_user = mongo.db.users.find_one(
                {"username": request.form.get("username").lower()})

            if existing_user:
                flash("Username already exists", 'error-msg')
                return redirect (url_for("register"))

            new_user = {
                "username": request.form.get("username").lower(),
                "password": generate_password_hash(request.form.get("password"))
            }
            mongo.db.users.insert_one(new_user)

            # put new user into 'session' cookie
            session["user"] = request.form.get("username").lower()
            flash("Registration Successful", 'success-msg')
            return redirect(url_for("profile", username=session["user"]))
        return render_template("register.html")

    flash("Passwords don't match", 'error-msg')
    return render_template("register.html")


@app.route("/signin", methods=["GET", "POST"])
def signin():
    '''function to sign in user if username exists'''
    if request.method == "POST":
        #check if username exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            #ensure hashed password matches
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                username = request.form.get("username")
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                #invalid password match
                flash("Incorrect Username/Password", 'error-msg')
                return redirect(url_for("signin"))

        else:
            #username doesn't exist
            flash("Incorrect Username/Password", 'error-msg')
    return render_template("signin.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    '''gets session user's username from db'''
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    return render_template("profile.html", username=username)


@app.route("/signout")
def signout():
    '''remove user from session cookie'''
    flash("You have been logged out", "success-msg")
    session.pop("user")
    return redirect(url_for("signin"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
