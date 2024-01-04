from flask import Flask
from flask_jwt_extended import JWTManager
from app.config import TestConfig
from app.server.auth.views.auth_views import auth_blueprint, AuthGroupAPI, AuthItemAPI
from app.server.auth.views.token_views import token_blueprint
from app.server.auth.models.user.user_model import User
from app.database import db


def create_app(default_config=TestConfig):
    """Define the Flask Application"""

    app = Flask(__name__)

    app.config.from_object(default_config)
    JWTManager(app)
    db.init_app(app)

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(token_blueprint)

    app.add_url_rule(
        "/auth_api/", endpoint="auth-group", view_func=AuthGroupAPI.as_view("auth_api_group", User)
    )
    app.add_url_rule(
        "/auth_api/<int:item_id>", endpoint="auth-item", view_func=AuthItemAPI.as_view("auth_api_item", User)
    )

    return app
