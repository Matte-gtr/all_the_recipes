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
    """ displays the home page as well as a list of available recipes"""
    return render_template('home_page.html', recipes=mongo.db.recipes.find())


@app.route("/create_account", methods=["GET", "POST"])
def create_account():
    """ displays the create account page/form """
    return render_template('create_account.html')


@app.route("/insert_account", methods=["POST"])
def insert_account():
    """ (from "create_account" submit) checks if the username is already in the
database and if the double entered passwords match, if the username is not
taken and the passwords match, a new user is created in the database """
    user = mongo.db.users.find_one({"user_name": request.form.get(
        'username').lower()})
    if user:
        flash('This username is taken')
        return redirect(url_for('create_account'))
    else:
        if request.form.get('password') == \
                request.form.get('confirm_password'):
            mongo.db.users.insert_one({
                "user_name": request.form.get('username').lower(),
                "email_address": request.form.get('email'),
                "password": request.form.get('password')
            })
            flash("account created")
        else:
            flash("Your passwords didn't match")
            return redirect(url_for('create_account'))
    return redirect(url_for('user_login'))


@app.route("/user_login", methods=["GET", "POST"])
def user_login():
    """ displays the login page/form """
    return render_template('user_login.html')


@app.route("/login", methods=["POST"])
def login():
    """ (from "user_login" submit) checks if the username is in the
    database and if so, that the passwords match, if the username is present
    and the passwords match, the user is logged in by way of storing the
    username in session """
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
