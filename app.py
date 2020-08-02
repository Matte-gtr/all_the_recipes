import os
from flask import Flask, render_template, url_for, session, redirect,\
    flash, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import datetime

app = Flask(__name__)

app.config["MONGO_DBNAME"] = "recipe_website"
app.config["MONGO_URI"] = os.getenv('MONGO_URI')

mongo = PyMongo(app)

app.secret_key = os.getenv('SECRET_KEY')


@app.route("/")
@app.route("/get_recipes")
def home_page():
    return render_template('home_page.html', recipes=mongo.db.recipes.find())


@app.route('/user_login', methods=["GET", "POST"])
def user_login():
    return render_template('user_login.html')


@app.route('/login', methods=["POST"])
def login():
    user = mongo.db.users.find_one({"user_name": request.form.get(
        'username').lower()})
    if user:
        if user['password'] == request.form.get('password'):
            session['username'] = user['user_name']
            return redirect(url_for('home_page'))
        else:
            flash('Incorrect password')
            return redirect(url_for('user_login'))
    else:
        flash('The username you entered does not exist')
        return redirect(url_for('user_login'))
    return render_template('home_page.html', user=mongo.db.users.find_one(
                            {'user_name': request.form.get('username')}))


if __name__ == "__main__":
    app.run(host=os.getenv("IP"),
            port=int(os.getenv("PORT")),
            debug=True)
