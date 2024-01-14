from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from flask.views import MethodView
from app.server.api.models.base import DBInterface
from app.server.api.models.user_model import User
from app.server.api.models.address_model import Address
from app.database import db
from sqlalchemy.exc import DisconnectionError


user_blueprint = Blueprint("user", __name__)


class UserItemView(MethodView):
    """Handles requests concerning groups of users."""

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

                user = DBInterface.get_object(User, id=new_user.id)
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


    def patch(self):
        pass

    def get(self):
        pass

    def delete(self):
        pass


class UserListView(MethodView):
    """Handles requests concerining single users."""

    @jwt_required()
    def get(self):

        interface = DBInterface(db.session)

        res = interface.join_tables_and_return_result(
            User, Address, User.id == Address.user_id,
            User.id, User.name, User.username, User.email,
            Address.street, Address.suite, Address.city,
            Address.zipcode, Address.lat, Address.long
        )

        if res or len(res) > 0:
            res_list = []
            for item in res:
                res_dict = item._asdict()
                cleaned_dict = {k: v for k, v in res_dict.items() if k != "User"}
                res_list.append(cleaned_dict)
            return jsonify({"data": res_list}), 200
        else:
            no_result_msg = "No results found."
            return jsonify({"msg": no_result_msg}), 200
