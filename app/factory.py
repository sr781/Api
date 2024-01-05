from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from app.config import DevConfig, TestConfig
from app.server.auth.views.auth_views import auth_blueprint, AuthGroupAPI, AuthItemAPI, LoginAPI
from app.server.auth.views.token_views import token_blueprint
from app.server.auth.models.user.user_model import User
from app.database import db

from datetime import timedelta


def create_app(default_config=TestConfig):
    """Define the Flask Application"""

    app = Flask(__name__)

    app.config.from_object(default_config)
    app.config["JWT_COOKIE_SECURE"] = False
    app.config["JWT_SECRET_KEY"] = "changeme"
    app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=45)
    app.config['JWT_COOKIE_CSRF_PROTECT'] = False

    JWTManager(app)
    CORS(app)
    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(auth_blueprint)
    # app.register_blueprint(token_blueprint)

    app.add_url_rule(
        "/auth_api/", endpoint="auth-group", view_func=AuthGroupAPI.as_view("auth_api_group", User)
    )
    app.add_url_rule(
        "/auth_api/<int:item_id>", endpoint="auth-item", view_func=AuthItemAPI.as_view("auth_api_item", User)
    )

    app.add_url_rule(
        "/auth_api/login", endpoint="auth-login", view_func=LoginAPI.as_view("auth_api_login", User)
    )

    return app
