import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


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


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
