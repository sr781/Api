"""
Flask Factory. Import, configure and return the Flask app.
"""
from flask import Flask
from app.database import db
from app.config import TestConfig


def create_app(default_config=TestConfig):
    """Create, configure and return the app."""

    app = Flask(__name__)
    app.config.from_object(default_config)

    db.init_app(app)
    with app.app_context():
        db.create_all() # Create tables in the DB.

    return app
