from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow


db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()


def create_app():
    app = Flask(__name__)
    # app.config.from_object(config_class)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"

    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)

    from app.api import bp as api_bp
    from app.main import bp as main_bp

    app.register_blueprint(api_bp, url_prefix="/api")
    app.register_blueprint(main_bp, url_prefix="/")

    return app
