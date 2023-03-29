from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# from config import Config


db = SQLAlchemy()
migrate = Migrate()

# from app import routes


def create_app():
    app = Flask(__name__)
    # app.config.from_object(config_class)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"

    db.init_app(app)
    migrate.init_app(app, db)

    from app.api import bp as api_bp

    app.register_blueprint(api_bp, url_prefix="/api")

    return app
