import os
from flask import (
    Flask, flash, render_template, Blueprint,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from lib.helper import db
if os.path.exists("env.py"):
    import env

blueprint = Blueprint("user", __name__, url_prefix="/user")


def existing_user():
    '''checks username against database'''
    return db().users.find_one(
            {"username": request.form.get("username").lower()})


def insert_new_user():
    '''Registers new user'''
    new_user = {
                "username": request.form.get("username").lower(),
                "password": generate_password_hash(
                    request.form.get("password"))
        }
    db().users.insert_one(new_user)


def update_password():
    '''changes users password'''
    return db().users.update_one(
                    {"username": session["user"]},
                    {"$set": {"password": generate_password_hash(
                        request.form.get("newPassword"))}}
                )


@blueprint.route("/register", methods=["GET", "POST"])
def register():
    '''Checks if password matches, if it does registers
     new user if they dont already exist'''
    if request.method == "POST":
        if request.form.get(
         "password") != request.form.get("confirm-password"):
            flash("Passwords don't match", 'error-msg')
            return render_template("register.html")
        # check if username exists
        if existing_user():
            flash("Username already exists", 'error-msg')
            return redirect(url_for("user.register"))
        # inserts new user into database
        insert_new_user()
        # put new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful", 'success-msg')
        return redirect(url_for("user.profile", username=session["user"]))
    return render_template("register.html")


@blueprint.route("/signin", methods=["GET", "POST"])
def signin():
    '''Signs in user if username exists'''
    if request.method == "POST":
        # check if username exists
        if existing_user():
            # ensure hashed password matches
            if check_password_hash(
              existing_user()["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                username = request.form.get("username")
                flash(f"Welcome, {username}", "success-msg")
                return redirect(url_for(
                    "user.profile", username=session["user"]))

        # username doesn't exist / Passwords wrong
        flash("Incorrect Username/Password", 'error-msg')
    return render_template("signin.html")


@blueprint.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    '''gets session user's username from db'''
    username = db().users.find_one(
        {"username": session["user"]})["username"]
    reviews = db().reviews.find(
        {"user": session["user"]})
    return render_template(
        "profile.html", username=username, reviews=reviews)


@blueprint.route("/signout")
def signout():
    '''remove user from session cookie'''
    flash("You have been logged out", "success-msg")
    session.pop("user")
    return redirect(url_for("user.signin"))


@blueprint.route("/delete_profile")
def delete_profile():
    '''takes user to confirm if they want to delete profile'''
    return render_template("delete_profile.html")


@blueprint.route("/delete_user")
def delete_user():
    '''Deletes user's profile/account along with all reviews'''
    db().reviews.delete_many({"user": session["user"]})
    db().users.delete_one({"username": session["user"]})
    session.pop("user")

    flash("Account deleted successfully", "success-msg")
    return redirect(url_for("register"))


@blueprint.route("/change_password")
def change_password():
    '''takes user to change password form'''
    return render_template("change_password.html")


@blueprint.route("/new_password", methods=["GET", "POST"])
def new_password():
    '''Checks user's password and if it is lets them change it'''
    user = db().users.find_one({"username": session["user"]})
    if request.method == "POST":
        if check_password_hash(
             user["password"], request.form.get("oldPassword")):
            password = request.form.get("newPassword")
            confirm_new_password = request.form.get("confirmNewPassword")
            if password == confirm_new_password:
                update_password()
                flash("password updated", "success-msg")
                return redirect(url_for(
                    "user.profile", username=session["user"]))

            flash("passwords don't match", "error-msg")
    return redirect(url_for("user.change_password"))
