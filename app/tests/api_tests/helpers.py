from app.server.api.models.user_model import User
from app.server.api.models.address_model import Address
from app.database import db


def create_user():
    """Helper method to create a test user.

    :param: None
    :return <User>
    """

    name = "Test User"
    username = "testusername"
    email = "test@example.com"
    phone = "1234567890"

    user = User(name=name, username=username, email=email, phone=phone)

    return user


def create_address(user_id):
    """
    Helper method to create a test address.

    :param user_id: ID of a test user to serve as FK.
    :return: <Address> object
    """

    street = "Test Street"
    suite = "Test Suite"
    city = "Test City"
    zipcode = "T35TZP"
    lat = "-3.01244"
    long = "24.34234"

    address = Address(user_id=user_id, street=street,
                      suite=suite, city=city, zipcode=zipcode,
                      lat=lat, long=long)

    return address
