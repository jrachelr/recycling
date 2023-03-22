from app import app
from flask import render_template, url_for
from app.models import Location, User, AcceptedItem

# Some fake data
locations = [
    {
        'name': 'goodwill',
        'address': '111 Pin Dr Ste A, IL, 00000'
    },
    {
        'name': 'church',
        'address': '222 My St Unit 9, CA, 111111'
    }
]


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


@app.route("/locations/all")
def all_locations():
    return render_template('locations.html', title='All Locations', locs=locations)
