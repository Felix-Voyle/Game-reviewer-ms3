import os
from flask import Flask, redirect
from flask_pymongo import PyMongo
if os.path.exists("env.py"):
    import env

# initialize the Flask app
app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


# initializing the client for mongodb
mongo = PyMongo(app)

# register blueprints
from .views import user
from .views import games

app.register_blueprint(user)
app.register_blueprint(games)


@app.route("/")
def index():
    return redirect("/games")