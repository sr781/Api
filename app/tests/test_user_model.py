from app.database import db
from app.tests.base import BaseTestCase
from app.server.auth.models.user.user_model import User
from werkzeug.security import check_password_hash

from unittest.mock import patch


class UserModelTests(BaseTestCase):
    def test_user_create_success(self, app):

        with app.app_context():
            user = User(
                email="test@example.com",
                password="testpass123"
            )
            db.session.add(user)
            db.session.commit()
            users = User.query.all()

            self.assertEqual(len(users), 1)
            self.assertEqual(users[0].email, "test@example.com")
            self.assertTrue(check_password_hash(users[0].password, "testpass123"))

    def test_user_delete_success(self, app):

        with app.app_context():
            user = User(
                email="test@example.com",
                password="testpass123"
            )
            db.session.add(user)
            db.session.commit()
            users = User.query.all()
            self.assertEqual(len(users), 1)

            user = db.session.get(User, ident=1)
            db.session.delete(user)
            db.session.commit()

            users = User.query.all()
            self.assertEqual(len(users), 0)

    @patch.object(User, "create_jwt_token")
    def test_create_jwt_token(self, app, patched_token):
        """Test creating JWT token for given user successful."""

        token_dict = {
            "access_token": "test_token"
        }

        with app.app_context():
            user = User(
                email="test@example.com",
                password="testpass123"
            )
            db.session.add(user)
            db.session.commit()
            user = db.session.get(User, ident=1)
            patched_token.return_value = token_dict
            token = User.create_jwt_token(user.email)
            self.assertEqual(token, token_dict)
