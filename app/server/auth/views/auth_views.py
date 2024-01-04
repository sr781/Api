from flask import request, jsonify, Blueprint
from flask.views import MethodView
from app.server.auth.models.user.user_model import User
from app.database import db


auth_blueprint = Blueprint("auth", __name__)


class AuthGroupAPI(MethodView):
    init_every_request = True

    def __init__(self, model: User):
        self.model = model

    @staticmethod
    def post():
        data = request.json
        try:
            email = data["email"]
            password = data["password"]

            user = User(email=email, password=password)
            if user.add_user():
                token = user.create_jwt_token()
                data["token"] = token
                return jsonify(data), 201
            msg = "Email address already exists."
            return jsonify({"msg": msg}), 400
        except KeyError:
            error_msg = "Please provide both an email and a password"
            return jsonify({"msg": error_msg}), 400


class AuthItemAPI(MethodView):

    def __init__(self, model):
        self.model = model

    def _get_item(self, item_id):
        return User.get_user(item_id)

    def get(self, item_id):
        user = self._get_item(item_id)
        return jsonify({"email": user.email}), 200
