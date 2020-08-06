import os
from flask import Flask, render_template, url_for, session, redirect,\
    flash, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import datetime
import pymongo
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.getenv('MONGO_URI')
app.secret_key = os.environ.get('SECRET_KEY')

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_recipes")
def home_page():
    """ displays the home page as well as a list of available recipes"""
    return render_template('home_page.html',
                           recipes=list(mongo.db.recipes.find().sort(
                               'updated_on', pymongo.ASCENDING)),
                           header="Check out our latest recipes")


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/text_search", methods=["GET", "POST"])
def text_search():
    search = request.form.get('search')
    recipes = list(mongo.db.recipes.find({'$text': {'$search': search}}))
    return render_template('home_page.html', recipes=recipes,
                           error_message='No recipes match the search "'
                           + search + '"')


@app.context_processor
def get_categories():
    """ returns a dict of categories to be listed in the navbar """
    return dict(categories=mongo.db.categories.find())


@app.route("/create_account", methods=["GET", "POST"])
def create_account():
    """ displays the create account page/form """
    return render_template('create_account.html')


@app.route("/insert_account", methods=["POST"])
def insert_account():
    """ (from "create_account" submit) checks if the username is already in the
database and if the double entered passwords match, if the username is not
taken and the passwords match, a new user is created in the database """
    existing_user = mongo.db.users.find_one({"user_name": request.form.get(
        'username').lower()})
    if existing_user:
        flash('This username is taken')
        return redirect(url_for('create_account'))
    else:
        if request.form.get('password') == \
                request.form.get('confirm_password'):
            mongo.db.users.insert_one({
                "user_name": request.form.get('username').lower(),
                "email_address": request.form.get('email'),
                "password": generate_password_hash(
                        request.form.get('password'))
            })
            flash("Account Created")
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
    existing_user = mongo.db.users.find_one({"user_name": request.form.get(
        'username').lower()})
    if existing_user:
        if check_password_hash(existing_user["password"],
                               request.form.get("password")):
            session['username'] = existing_user['user_name']
            return redirect(url_for('home_page'))
        else:
            flash('Incorrect password')
            return redirect(url_for('user_login'))
    else:
        flash('The username you entered does not exist')
        return redirect(url_for('user_login'))
    return render_template('home_page.html', user=mongo.db.users.find_one(
                            {'user_name': request.form.get('username')}))


@app.route('/logout')
def logout():
    """ logs user out by removing username from session, redirects
    to home page """
    session.pop('username', None)
    return redirect(url_for('home_page'))


@app.route('/create_recipe')
def create_recipe():
    return render_template('create_recipe.html',
                           cats=mongo.db.categories.find())


@app.route("/insert_recipe", methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    current_time = datetime.datetime.now().strftime('%X %x')
    recipes.insert_one({
        'category': request.form.get('category'),
        'recipe_name': request.form.get('recipe_name'),
        'description': request.form.get('description'),
        'ingredients': request.form.getlist('ingredients'),
        'method': request.form.getlist('method'),
        'required_tools': request.form.getlist('tools'),
        'servings': request.form.get('servings'),
        'preparation_time': request.form.get('preparation_time'),
        'cook_time': request.form.get('cook_time'),
        'image_url': request.form.get("image_url"),
        'created_on': current_time,
        'updated_on': current_time,
        'owner': session['username']
    })
    return redirect(url_for('home_page'))


@app.route('/recipes_by_category/<category>')
def recipes_by_category(category):
    recipes = list(mongo.db.recipes.find({'category': category}).sort(
        'updated_on', pymongo.ASCENDING))
    return render_template('home_page.html', recipes=recipes,
                           header="All " + category.capitalize() + " Recipes",
                           error_message="No results for "
                           + category.capitalize())


@app.route('/user_recipes/<owner>')
def user_recipes(owner):
    recipes = list(mongo.db.recipes.find({'owner': session['username']}).sort(
        'updated_on', pymongo.ASCENDING))
    return render_template('home_page.html', recipes=recipes,
                           header="All " + owner.capitalize() + " Recipes",
                           error_message=owner.capitalize()
                           + " currently has no recipes")


@app.route('/view_recipe/<recipe_id>')
def view_recipe(recipe_id):
    return render_template('view_recipe.html',
                           recipe=mongo.db.recipes.find_one({
                            '_id': ObjectId(recipe_id)}))


@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    return render_template('edit_recipe.html',
                           recipe=mongo.db.recipes.find_one({
                            '_id': ObjectId(recipe_id)}),
                           cats=mongo.db.categories.find())


@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    current_time = datetime.datetime.now().strftime('%X %x')
    mongo.db.recipes.update({'_id': ObjectId(recipe_id)},
                            {'$set': {
                                'category': request.form.get('category'),
                                'recipe_name': request.form.get('recipe_name'),
                                'description': request.form.get('description'),
                                'ingredients': request.form.getlist(
                                    'ingredients'),
                                'method': request.form.getlist('method'),
                                'required_tools': request.form.getlist(
                                    'tools'),
                                'servings': request.form.get('servings'),
                                'preparation_time': request.form.get(
                                    'preparation_time'),
                                'cook_time': request.form.get('cook_time'),
                                'image_url': request.form.get("image_url"),
                                'updated_on': current_time,
                            }})
    return redirect(url_for('view_recipe', recipe_id=recipe_id))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
