from flask import request, jsonify, Blueprint
from flask.views import MethodView
from app.server.auth.models.user.user_model import AuthUser
from flask_jwt_extended import get_jwt_identity, set_access_cookies, get_jwt, jwt_required, verify_jwt_in_request


auth_blueprint = Blueprint("auth", __name__)


class AuthGroupAPI(MethodView):
    init_every_request = True

    def __init__(self, model: AuthUser):
        self.model = model

    @staticmethod
    def post():
        data = request.json
        try:
            email = data["email"]
            password = data["password"]

            user = AuthUser(email=email, password=password)
            if user.add_user():
                token = user.create_jwt_token()
                resp = jsonify({"msg": "registration successful"})
                set_access_cookies(resp, token)
                data["token"] = token
                print("New user created.")
                return resp, 201
            else:
                print("hello.......")
                msg = "Email address already exists."
                return jsonify({"msg": msg}), 400
        except KeyError:
            error_msg = "Please provide both an email and a password"
            return jsonify({"msg": error_msg}), 400


class AuthItemAPI(MethodView):

    def __init__(self, model):
        self.model = model

    @staticmethod
    def _get_item(item_id):
        return AuthUser.get_user(item_id)

    @jwt_required()
    def get(self, item_id):
        user = self._get_item(item_id)
        if user:
            print("FOUND USER:", user)
            return jsonify({"email": user.email}), 200
        else:
            print("USER NOT FOUND")
            return 400


class LoginAPI(MethodView):
    """View to log in a user."""

    def __init__(self, model):
        self.model = model

    @staticmethod
    def post():
        """Login user"""

        data = request.json
        try:
            email = data["email"]
            password = data["password"]

            user = AuthUser(email=email, password=password)
            db_result = user.get_user_with_credentials(password)

            if isinstance(db_result, AuthUser):
                token = user.create_jwt_token()
                success_msg = "Login successful."
                user_dict = {"msg": success_msg}

                user_dict["id"] = db_result.id
                resp = jsonify(user_dict)
                set_access_cookies(resp, token)
                return resp, 200
            elif db_result == "not found":
                error_msg = "Email not found. Please try again."
                return jsonify({"msg": error_msg}), 400
            else:
                error_msg = "Incorrect password. Please try again."
                return jsonify({"msg": error_msg}), 400

        except KeyError:
            error_msg = "Please provide both an email and a password."
            return jsonify({"msg": error_msg}), 400





