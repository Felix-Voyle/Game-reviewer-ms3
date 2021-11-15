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
    '''requests game data from api'''
    parameters = {
        "page_size": 12
    }
    response = requests.get(
        f"https://api.rawg.io/api/games?key={API_KEY}", params=parameters)
    data = response.json()

    return render_template("games.html", data=data)


@app.route("/search", methods=["GET", "POST"])
def search():
    '''Allows user to search games using the rawg API as the database'''
    query = request.form.get("query")
    parameters = {
        "page_size": 12,
        "search": f"{query}"
    }
    response = requests.get(
        f"https://api.rawg.io/api/games?key={API_KEY}", params=parameters)
    data = response.json()

    return render_template("games.html", data=data)


@app.route("/get_reviews")
def get_reviews():
    '''Shows list of reviews from Mongodb'''
    reviews = mongo.db.reviews.find()
    return render_template("reviews.html", reviews=reviews)


@app.route("/register", methods=["GET", "POST"])
def register():
    '''Checks if password matches, if it does registers
     new user if they dont already exist'''
    if request.method == "POST":
        if request.form.get(
         "password") != request.form.get("confirm-password"):
            flash("Passwords don't match", 'error-msg')
            return render_template("register.html")
        # check if username exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists", 'error-msg')
            return redirect(url_for("register"))

        new_user = {
                "username": request.form.get("username").lower(),
                "password": generate_password_hash(
                    request.form.get("password"))
        }
        mongo.db.users.insert_one(new_user)

        # put new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful", 'success-msg')
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/signin", methods=["GET", "POST"])
def signin():
    '''Signs in user if username exists'''
    if request.method == "POST":
        # check if username exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches
            if check_password_hash(
              existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                username = request.form.get("username")
                flash(f"Welcome, {username}", "success-msg")
                return redirect(url_for(
                    "profile", username=session["user"]))

        # username doesn't exist / Passwords wrong
        flash("Incorrect Username/Password", 'error-msg')
    return render_template("signin.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    '''gets session user's username from db'''
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    reviews = mongo.db.reviews.find(
        {"user": session["user"]})
    return render_template("profile.html", username=username, reviews=reviews)


@app.route("/signout")
def signout():
    '''remove user from session cookie'''
    flash("You have been logged out", "success-msg")
    session.pop("user")
    return redirect(url_for("signin"))


@app.route("/add_review", methods=["GET", "POST"])
def add_review():
    '''adds review to db'''
    if request.method == "POST":
        already_reviewed = {
            "game_name": request.form.get("game_name"),
            "user": session["user"]
        }
    check_exists = mongo.db.reviews.find_one(already_reviewed)
    if check_exists is None:
        review = {
            "game_name": request.form.get("game_name"),
            "game_rating": request.form.get("rating"),
            "game_img": request.form.get("game_img"),
            "user": session["user"],
            "game_review": request.form.get("review")
        }
        mongo.db.reviews.insert_one(review)
        flash("Review added successfully", "success-msg")
        return redirect(url_for("get_reviews"))

    flash("You've Already reviewed this game", "error-msg")
    return redirect(url_for("get_reviews"))


@app.route("/edit_review/<review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    '''Finds review by id and edits it'''
    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    if request.method == "POST":
        edit = {
            "game_name": request.form.get("game_name"),
            "game_rating": request.form.get("rating"),
            "game_img": request.form.get("game_img"),
            "user": session["user"],
            "game_review": request.form.get("review")
        }

        mongo.db.reviews.update({"_id": ObjectId(review_id)}, edit)
        flash("Review updated successfully", "success-msg")
        return redirect(url_for("get_reviews"))

    return render_template("edit_review.html", review=review)


@app.route("/delete_review/<review_id>")
def delete_review(review_id):
    '''Deletes Review by id'''
    mongo.db.reviews.delete_one({"_id": ObjectId(review_id)})
    flash("Review deleted successfully", "success-msg")
    return redirect(url_for("get_reviews"))


@app.route("/delete_user")
def delete_user():
    '''Deletes user's profile/account'''
    mongo.db.reviews.delete_many({"user": session["user"]})
    mongo.db.users.delete_one({"username": session["user"]})
    session.pop("user")

    flash("Account deleted successfully", "success-msg")
    return redirect(url_for("register"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
