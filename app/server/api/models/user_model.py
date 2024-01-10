from app.database import db
from sqlalchemy.exc import OperationalError, IntegrityError
import time


class User(db.Model):
    """Model to represent a User model in DB."""
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), nullable=False)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    phone = db.Column(db.String(50), nullable=True)
    addresses = db.relationship("Address", backref="user", lazy=True)

    def __init__(self, name, username, email, phone):
        self.name = name
        self.username = username,
        self.email = email,
        self.phone = phone

    def add_user(self):
        """TODO: TEST OPERATIONAL FAILURE"""
        num_retries = 5
        user_registration_success = False

        while num_retries > 0:
            try:
                self.commit(self)
                user_registration_success = True
                break
            except OperationalError:
                num_retries -= 1
                time.sleep(1)
            except IntegrityError:
                print('Integrity error raised')
                db.session.rollback()
                return False

        if not user_registration_success:
            return False
        return True

    @staticmethod
    def commit(obj):
        db.session.add(obj)
        db.session.commit()