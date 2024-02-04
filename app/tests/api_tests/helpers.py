from app.server.api.models.user_model import User
from app.server.api.models.address_model import Address
from app.database import db


def create_user(name="Test User", username="testusername",
                email="test@example.com", phone="1234567890"):
    """Helper method to create a test user.

    :param name
    :param username
    :param email
    :param phone

    :return <User>
    """

    user = User(name=name, username=username, email=email, phone=phone)

    return user


def create_address(user_id, street="Test Street", suite="Test Suite",
                   city="Test City", zipcode="T35TZP",
                   lat="-3.01244", long="24.34234"):
    """
    Helper method to create a test address.

    :param user_id
    :param street
    :param suite
    :param city
    :param zipcode
    :param lat
    :param long

    :return <Address>
    """

    address = Address(user_id=user_id, street=street,
                      suite=suite, city=city, zipcode=zipcode,
                      lat=lat, long=long)

    return address
