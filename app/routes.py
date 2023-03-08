from app import app
from flask import render_template, url_for

# Some fake data


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title='Home')


@app.route("/about")
def about():
    return render_template('about.html', title='About')

# TODO: User specific routes


@app.route("/register")
def register():
    return 'register'


@app.route("/login")
def login():
    return 'Login'


@app.route("/logout")
def logout():
    return 'Logout'


@app.route("/account")
def account():
    return 'account'

# TODO: Location specific routes
    return 'About'


@app.route("/locations")
def locations():
    return 'locations'
