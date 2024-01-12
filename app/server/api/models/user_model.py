from app.database import db
from app.server.api.models.base import DBInterface
from sqlalchemy.orm import Mapped


class User(db.Model):
    """Model to represent a User model in DB."""
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = db.Column(db.String(200), nullable=False)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    phone = db.Column(db.String(50), nullable=True)
    addresses = db.relationship("Address", backref="user", cascade="delete, all", lazy=True)

    def __init__(self, name, username, email, phone):
        self.name = name
        self.username = username,
        self.email = email,
        self.phone = phone

    @staticmethod
    def get_user(username):
        interface = DBInterface(db.session)
        user = interface.get_object(User, username=username)
        if user:
            return user
        else:
            return None

    def insert(self):
        interface = DBInterface(db.session)
        insertion_attempt = interface.add_to_db(self)
        if insertion_attempt:
            return True
        else:
            return None

    @staticmethod
    def remove(user_model):
        interface = DBInterface(db.session)
        delete_attempt = interface.remove_from_db(user_model)
        if delete_attempt:
            return True
        else:
            return None

    @staticmethod
    def update(user_model, attrs):
        interface = DBInterface(db.session)
        update_attempt = interface.update_object(user_model, attrs)
        print(update_attempt)
        if update_attempt:
            return True
        else:
            return None
