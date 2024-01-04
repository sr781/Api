from app.database import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from sqlalchemy.exc import NoResultFound


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __init__(self, email, password):
        self.email = email
        self.password = generate_password_hash(password)

    @staticmethod
    def get_user(email, password):
        try:
            user = db.session.get(User, ident={"email": email})
            if check_password_hash(user.password, password):
                return user
            else:
                return False
        except NoResultFound:
            return False

    @staticmethod
    def create_jwt_token(email):
        return create_access_token(identity=email)

    def add_user(self):
        db.session.add(self)
        db.session.commit()
