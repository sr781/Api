from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from flask.views import MethodView
from app.server.api.models.base import DBInterface
from app.server.api.models.user_model import User
from app.server.api.models.address_model import Address
from app.server.api.models.schemas.user_schema import UserSchema
from app.database import db
from sqlalchemy.exc import DisconnectionError


user_blueprint = Blueprint("user", __name__)


class UserItemView(MethodView):
    """Handles requests concerning groups of users."""

    def patch(self):
        pass

    @jwt_required()
    def get(self, user_id):
        """Get a single user."""

        interface = DBInterface(db.session)
        user = interface.get_object(User, id=user_id)
        user_schema = UserSchema(many=False)
        data = user_schema.dump(user)

        return jsonify({"data": data}), 200

    def delete(self):
        pass


class UserListView(MethodView):
    """Handles requests concerining single users."""

    @jwt_required()
    def get(self):

        interface = DBInterface(db.session)
        users = interface.get_all_objects(User)

        if len(users) > 0:
            user_schema = UserSchema(many=True)
            data = user_schema.dump(users)

            return jsonify({"data": data}), 200
        else:
            msg = "No results found."
            return jsonify({"msg": msg}), 200

    @jwt_required()
    def post(self):
        data = request.json
        interface = DBInterface(db.session)

        try:
            name = data["name"]
            username = data["username"]
            email = data["email"]
            phone = data["phone"]

            new_user = User(name, username, email, phone)
            interface.add_to_db(new_user)

            if "address" in data:
                street = data["address"]["street"]
                suite = data["address"]["suite"]
                city = data["address"]["city"]
                zipcode = data["address"]["zipcode"]
                lat = data["address"]["lat"]
                long = data["address"]["long"]

                user = interface.get_object(User, id=new_user.id)
                address = Address(user.id, street, suite, city, zipcode, lat, long)
                interface.add_to_db(address)

            success_msg = "New user created."
            return jsonify({"msg": success_msg}), 201
        except KeyError:
            error_msg = "Some details are missing. Please try again"
            return jsonify({"msg": error_msg})
        except DisconnectionError:
            error_msg = "Database disconnected, please try again."
            return jsonify({"msg": error_msg})