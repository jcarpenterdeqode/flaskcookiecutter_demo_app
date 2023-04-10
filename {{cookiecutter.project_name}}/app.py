"""App entry point."""
"""Initialize Flask app."""
import os
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

db = SQLAlchemy()
mail = Mail()



"""Flask configuration variables."""
from os import environ, path

from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))


class Config:
    """Set Flask configuration from .env file."""

    # General Config
    JWT_SECRET_KEY = environ.get("SECRET_KEY")


    # Database
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


def create_app(testing=False):
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    mail = Mail(app)
    
    if testing is True:
        app.config["TESTING"] = True

    # This is the configuration for the email server.
    app.config["MAIL_SERVER"] = "smtp.gmail.com"
    app.config["MAIL_PORT"] = 465
    app.config["MAIL_USERNAME"] = os.environ.get("EMAIL_HOST_USER")
    app.config["MAIL_PASSWORD"] = os.environ.get("EMAIL_HOST_PASSWORD")
    app.config["MAIL_USE_TLS"] = False
    app.config["MAIL_USE_SSL"] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = environ.get("SQLALCHEMY_DATABASE_URI")
    app.config['FLASK_DEBUG'] = environ.get("FLASK_DEBUG")

    if testing is True:
        app.config["TESTING"] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = environ.get("SQLALCHEMY_DATABASE_URI")

    mail = Mail(app)
    
    app.config_class = Config
    api = Api(app=app)

    from {{cookiecutter.project_name}}.users.routes import create_authentication_routes

    create_authentication_routes(api=api)

    db.init_app(app)

    with app.app_context():
        db.create_all()  # Create database tables for our data models

        return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)