import os
from flask import Flask, render_template, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import datetime

app = Flask(__name__)

app.config["MONGO_DBNAME"] = "recipe_website"
app.config["MONGO_URI"] = os.getenv('MONGO_URI')

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_recipes")
def home_page():
    return render_template('home_page.html', recipes=mongo.db.recipes.find())


@app.route('/login')
def login():
    return render_template('login.html', methods="POST")


if __name__ == "__main__":
    app.run(host=os.getenv("IP"),
            port=int(os.getenv("PORT")),
            debug=True)
