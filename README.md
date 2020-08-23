# All the Recipes

The "All the Recipes" website was created to give users a base to view other users recipes and be able to filter the recipes based on category or search 
through them using the ingredient search. The user also has the ability to create an account, which will allow them to add their own recipes
for other users to view. If a user is logged in, they can also filter for recipes that they have created and when viewing them, they are presented 
with the options to edit or remove the recipe. Once a recipe has been removed, it will be stored in the users "Removed recipes", hidden from public 
view. From this point, they can either re-publish the recipe or delete it from the database entirely. There is also a tools page where users are shown
a brief outline of some spondored tools/utensils and can be redirected to a different site to purchase these.

## UX

This website is aimed at users who are generally in their 20s and older, who are interested in trying out new recipes and potentially sharing some of 
their own recipes with other users. The interface is designed to suit all platforms ranging from mobile phones to desktop, using a mobile first approach.
No functionality/visability of lost when viewing this site on a smaller device such as a mobile phone.

The website features a navigation bar that collapses into a burger button on smaller devices, which is permenantly fixed to the top of the screen so users
access any part of the site no matter where they are on a particular page. The display of the recipes is designed to change slightly depending on who is 
viewing the recipe and if they are logged in or not, the creator of the recipe will have options available to them at the bottom of the screen.

If a user who is not logged in tries to create a recipe, they will be redirected to the login page and will return to the "create recipe" page once they
have successfully logged in.

#### User story:
I am presented with a screen showing me a variety of recipes to view with some basic details displayed.

#### User story:
When i see a recipe I like, I want to click on the recipe to view the full details.

#### User story:
I want to be able to create or add my own recipes for other users to view.

#### User story:
I want to be able to remove one of my recipes if I am not happy with it or I want to make some changes to it before I share it with other users.

#### User story:
I want to be able to delete a recipe completely.

#### User story:
I can be redirected to a page where I can purchase cooking utensils if I like the sound of them.

The wireframes/initial mockups for the "All the Recipes" website can be found here: https://github.com/Matte-gtr/all_the_recipes/tree/master/static/images/wireframes

## Features

* Home Page - This is the first page a user will see when visiting the site, the page displays all of the most recently updated recipes in the 
form of "cards" that the user can click on to be directed to the recipe page containing the full details of the recipe. This page also displays  
the search results for the ingredient search, user filter and category filter. There are 12 recipes displayed on the home page with pagination links
at the bottom of the page to view older recipes

* Tools Page - This page is accessed from the navbar and recipe pages, it contains an overview of some different types of tools/utensils relating 
to cooking and baking. The user can be directed to the website selling the tools by clicking on the "view range" button.

* Add Recipe Page - This page can be accessed from the navbar, however the user will be redirected to the login page if they aren't currently
logged in. This page contains a form that can be filled out by the user and upon submission of the form, this will be added to the list of recipes
that can be viewed by all users.

* Categories Dropdown - This is displayed in the form of a button on the navbar which when clicked, will reveal a list of all the available categories 
of active recipes on the site. When a category is clicked, the results are displayed in the same format as the home page recipes, but will only display
the recipes matching that particular category.

* Sign up button/page - This page is accessed from the navbar, only for users who aren't currently logged in. A user will be asked to choose a username,
add their email address, input a password and confirm their password. If the user enters a username that is already taken, they will be notified of this
and can choose a different username. Once the form is completed successfully, the user will be redirected to the login page so they can log in.

* Login button/page - This page is accessed from the navbar, only for users who aren't currently logged in. A user will be asked to enter their username
and password to log in. If they enter an incorrect password or username, they will be notified of this and can try again. On successful completion of the
form, they will be logged in a redirected to the home page, unless they were redirected to the login page from the Add Recipe button.

* User Option - This button will replace the Login/Sign up buttons on the navbar once the user is logged in. when this button is clicked, the user will be 
presented with a dropdown list of three options: "My recipes", "Removed Recipes" and "Log out".

* My Recipes button - This button works in much the same way as the categories dropdown, but the user will be presented with all the recipes they have 
created (if they have not been removed). From here they will be able to click on a card and view each recipe and the recipes will contain options at the
bottom of the recipe to edit or remove the recipe.

* Removed Recipes button  - This button works in the same way as the "My Recipes" button, but will display all recipes that the user has removed. If a recipe 
card is clicked on, the options at the bottom of the recipe will now show "Re-publish" and "Delete".

* Log out - This button can be found on the navbar, user the user options, only for users who are logged in. This button will log the user out, meaning they 
will not be able to edit their recipes (if they have any) or create any new recipes.

## Features left to implement:

* Auto hyperlink of tools in each recipe - If the tool is available on the tools page, the particlar tool will be hyperlinked to redirect the user to the 
external site that sells the tool.

* Recipe voting - a voting system that will allow users to "like" the recipe, giving the creator some feedback on what users think of their recipes.

## Technologies Used

HTML5

CSS3

Bootstrap
https://getbootstrap.com/docs/4.4/getting-started/introduction/
Bootstrap was used to speed up the development time and make use of their grid system for responsive mobile first design.

Google fonts
https://fonts.google.com/
Google fonts was used to provide all the fonts for the site as they have a very large library of fonts

JavaScript

JQuery
The project uses JQuery to simplify DOM manipulation.

FontAwesome
https://fontawesome.com/icons?d=gallery

Python3

Flask

Pymongo

MongoDB/Atlas

Flask-Paginate
Flask-paginate was used to simplify the process of paginating the recipe results on the home page.

werkzeug.security
For password hashing

## Automated testing

The automated test file can be found here: https://github.com/Matte-gtr/all_the_recipes/blob/master/tests.py
For details on how to run the tests, please see below in deplayment *
All tests contain docstrings for clear descriptions of what is being tested.

## Manual Testing

During the creation of this project, Google Chrome developer tools was used to view the site/pages on various different devices.
The developer tools displays used were: Galaxy S5, Pixel 2, Pixel 2 XL, iPhone 5/se, iPhone X, iPhone 6/7/8, iPhone 6/7/8 Plus, iPad, iPad Pro.
These were checked at multiple points throughout the development and then once again on all the above devices when the project was completed.

The site was also tested on various actual devices listed below once the site was completed:
* Asus Laptop
* Dell Laptop
* Samsung Galaxy S9
* iPhone 8
* Samsung tablet
* iPhone 10

The site was then tested on 4 different browsers:
* Google Chrome
* Internet Explorer
* Mozilla Firefox
* Apple Safari

The site was also tested for fast user learning by asking 3 different people to use the site and create, then remove and delete a recipe.
The reaction was reasonably good, with one comment on adding in a description on how to remove and delete your recipes. This will be implemented
at a later date on the removed_recipes display page.

## Database Schema
The database is structured with three collections, recipes, categories and users. The recipes and users collections are related by recipes(owner) and 
users(user_name), while the recipes and categories collections are related by category.

## Deployment
This project was Deployed using Heroku.

To Clone the project from github, use:
$ git clone https://github.com/Matte-gtr/all_the_recipes.git

I recommend deploying the project in a virtual envioronment:
$ cd directory-name
$ python3 -m venv virtual-env-name

You will need to install the dependencies found in the requirements.txt file:
$ pip3 install -r requirements.txt 

To run the project locally use:
$ python3 app.py

You can also run the app through Heroku.
https://all-the-recipes.herokuapp.com

This will run the automated tesing file
$python3 tests.py

#### Credits
Google Images - background images used across the site
Freecodecame - examples and explanations of using multiple functions 
w3schools - General learning material and descriptions
Flask documentation - For information on flask functionality
Stack Overflow - code snippets were taken and modified from here
Lakeland.co.uk - Used as the chosen tool supplier, images were used from their website for the tools page

#### Content
All recipes - Some recipes were added to the site with images and information being taken from https://www.bbcgoodfood.com/recipes.
Lakeland - Images of tools and descriptions taken from https://www.lakeland.co.uk/.

The inspiration for this site primarily came from https://www.oola.com/.