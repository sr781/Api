from flask import Flask
from flask_jwt_extended import JWTManager
from app.server.config import TestConfig
from app.server.api.views import auth_blueprint, AuthAPI
from app.server.auth.models.user.user_model import User
from app.database import db as flask_db


def create_app(default_config=TestConfig):
    """Define the Flask Application"""

    app = Flask(__name__)

    app.config.from_object(default_config)
    JWTManager(app)
    db = flask_db.init_app(app)

    app.register_blueprint(auth_blueprint)

    app.add_url_rule("/auth_api/", endpoint="auth", view_func=AuthAPI.as_view("auth_api", User))

    return app, db
