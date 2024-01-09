from flask import Flask
from flask_jwt_extended import JWTManager
from app.config import TestConfig
from app.server.auth.views.auth_views import auth_blueprint, AuthGroupAPI, AuthItemAPI, LoginAPI
from app.server.auth.models.user.user_model import AuthUser
from app.database import db

from datetime import timedelta


def create_app(default_config=TestConfig):
    """
    Define the Flask Application
    :param default_config - Defaults to TestConfig for unit tests.
    :return Flask app

    Initialize:
        - Flask app
        - JWT Manager
        - CORS

    Register blueprints:
        - Auth
        - User

    Register routes:
        - Auth:
            - Auth group
            - Auth item
        - User:
            - TODO: User group
            - TODO: User item
        - Post:
            - TODO: Post group
            - TODO: Post item
    """

    app = Flask(__name__)

    app.config.from_object(default_config)
    app.config["JWT_COOKIE_SECURE"] = False
    app.config["JWT_SECRET_KEY"] = "changeme"
    app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(seconds=10)
    app.config['JWT_COOKIE_CSRF_PROTECT'] = False

    db.init_app(app)
    JWTManager(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(auth_blueprint)
    # app.register_blueprint(token_blueprint)

    app.add_url_rule(
        "/auth_api/", endpoint="auth-group", view_func=AuthGroupAPI.as_view("auth_api_group", AuthUser)
    )
    app.add_url_rule(
        "/auth_api/<int:item_id>", endpoint="auth-item", view_func=AuthItemAPI.as_view("auth_api_item", AuthUser)
    )

    app.add_url_rule(
        "/auth_api/login", endpoint="auth-login", view_func=LoginAPI.as_view("auth_api_login", AuthUser)
    )

    return app
