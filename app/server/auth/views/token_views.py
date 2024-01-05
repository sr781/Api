from app.server.auth.models.user.user_model import User
from flask_jwt_extended import get_jwt_identity, set_access_cookies, get_jwt
from datetime import datetime, timedelta
from flask import Blueprint


token_blueprint = Blueprint("tokens", __name__)


@token_blueprint.after_request
def refresh(response):

    try:
        exp = get_jwt()["exp"]
        now = datetime.now()
        timestamp = datetime.timestamp(now + timedelta(seconds=5))
        if timestamp > exp:
            print("HELLO!")
            access_token = User.refresh_jwt_token(get_jwt_identity)
            set_access_cookies(response, access_token)
            return response
    except (RuntimeError, KeyError):
        return response
