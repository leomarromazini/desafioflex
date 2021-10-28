from os import environ
from flask import Flask
from dotenv import load_dotenv

load_dotenv()


def init_app(app: Flask):

    app.config["SQLALCHEMY_DATABASE_URI"] = environ.get("SQLALCHEMY_DATABASE_URI")

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = bool(
        environ.get("SQLALCHEMY_TRACK_MODIFICATIONS")
    )

    if environ.get('FLASK_ENV') == 'production':
        app.config["SQLALCHEMY_DATABASE_URI"] = environ.get('DATABASE_URL').replace("postgres", "postgresql")
    else:
        app.config["SQLALCHEMY_DATABASE_URI"] = environ.get("SQLALCHEMY_DATABASE_URI")