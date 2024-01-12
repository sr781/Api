from app.database import db
from app.server.api.models.base import DBInterface


class Address(db.Model):
    """Model to represent an Address record in DB."""
    __tablename__= "addresses"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    street = db.Column(db.String(200), nullable=True)
    suite = db.Column(db.String(125), nullable=True)
    city = db.Column(db.String(80), nullable=True)
    zipcode = db.Column(db.String(20), nullable=True)
    lat = db.Column(db.String(20), nullable=True)
    long = db.Column(db.String(20), nullable=True)

    def __init__(self, user_id, street, suite, city,
                 zipcode, lat, long):
        self.user_id = user_id
        self.street = street
        self.suite = suite
        self.city = city
        self.zipcode = zipcode
        self.lat = lat
        self.long = long

    def insert(self):
        interface = DBInterface(db.session)
        insertion_attempt = interface.add_to_db(self)
        if insertion_attempt:
            return True
        else:
            return None

    @staticmethod
    def get_address(address_id):
        interface = DBInterface(db.session)
        address = interface.get_object(Address, id=address_id)
        if address:
            return address
        else:
            return None

    @staticmethod
    def remove(address_model):
        interface = DBInterface(db.session)
        delete_attempt = interface.remove_from_db(address_model)
        if delete_attempt:
            return True
        else:
            return None

    @staticmethod
    def update(address_model, attrs):
        interface = DBInterface(db.session)
        update_attempt = interface.update_object(address_model, attrs)
        if update_attempt:
            return True
        else:
            return None
