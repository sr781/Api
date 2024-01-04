from flask import request, jsonify, Blueprint
from flask.views import MethodView
from app.server.auth.models.user.user_model import User


auth_blueprint = Blueprint("auth", __name__)


class AuthAPI(MethodView):
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
            user.add_user()
            return jsonify(data), 201
        except KeyError:
            error_msg = "Please provide both an email and a password"
            return jsonify({"msg": error_msg}), 400
