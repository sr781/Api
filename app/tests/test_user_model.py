from app.server import db, app as flask_app
from app.tests.base import BaseTestCase
from app.server.models.user.models import User
from werkzeug.security import check_password_hash


def create_user(email="test@example.com", password="testpass123"):
    with flask_app.app_context():
        user = User(
            email=email,
            password=password
        )
        db.session.add(user)
        db.session.commit()
        return user


class UserModelTests(BaseTestCase):
    def test_user_create_success(self, app):
        create_user()

        with flask_app.app_context():
            users = User.query.all()

            self.assertEqual(len(users), 1)
            self.assertEqual(users[0].email, "test@example.com")
            self.assertTrue(check_password_hash(users[0].password, "testpass123"))

    def test_user_delete_success(self, app):

        create_user()

        with flask_app.app_context():
            users = User.query.all()
            self.assertEqual(len(users), 1)

            user = db.session.get(User, ident=1)
            db.session.delete(user)
            db.session.commit()

            users = User.query.all()
            self.assertEqual(len(users), 0)
