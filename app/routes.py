from app import app


@app.route("/")
@app.route("/home")
def hello_world():
    return "<p>Hello, World!</p>"
