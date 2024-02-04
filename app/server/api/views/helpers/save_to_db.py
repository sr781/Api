from app.server.api.models.user_model import User
from app.server.api.models.address_model import Address
from sqlalchemy.exc import DisconnectionError


def write_user(interface, data):
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
            return {
                "success_msg": success_msg
            }
    except KeyError:
        error_msg = "Some details are missing. Please try again"
        return {
            "error_msg": error_msg
        }
    except DisconnectionError:
        error_msg = "Database disconnected, please try again."
        return {
            "error_msg": error_msg
        }
