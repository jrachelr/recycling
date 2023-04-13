from app.main import bp
from flask import render_template, url_for


@bp.route("/")
@bp.route("/home")
def home():
    return 'Hello World!'


@bp.route("/about")
def about():
    return render_template("about.html", title="About")


@bp.route("/register")
def register():
    return "register"


@bp.route("/login")
def login():
    return "Login"


@bp.route("/logout")
def logout():
    return "Logout"


@bp.route("/account")
def account():
    return "account"
