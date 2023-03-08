from app import app
from flask import redirect, render_template


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title='Home')


@app.route("/about")
def about():
    return 'Aboyut'

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
