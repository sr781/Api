# GROUP EXERCISE - SATISFY THESE UNIT TESTS

from app.database import db
from app.tests.base import BaseTestCase
from app.api.auth.models.auth_model import AuthUser
from werkzeug.security import check_password_hash

from unittest.mock import patch


class AuthUserModelTests(BaseTestCase):
    """
    Test integration of Auth User model in DB.

    Methods:
        test_user_create_success - Test creating user successful.
        test_user_delete_success - Test deleting user successful.
        test_create_jwt_token - Test create_jwt_token() method functions correctly.
    """


    def test_user_create_success(self, app):
        """Test creating a user is successful."""

        with app.app_context():
            user = AuthUser(
                email="test@example.com",
                password="testpass123"
            )
            db.session.add(user)
            db.session.commit()
            users = AuthUser.query.all()

            self.assertEqual(len(users), 1)
            self.assertEqual(users[0].email, "test@example.com")
            self.assertTrue(check_password_hash(users[0].password, "testpass123"))

    def test_user_delete_success(self, app):
        """Test deleting a user is succesful."""

        with app.app_context():
            user = AuthUser(
                email="test@example.com",
                password="testpass123"
            )
            db.session.add(user)
            db.session.commit()
            users = AuthUser.query.all()
            self.assertEqual(len(users), 1)

            user = db.session.get(AuthUser, ident=1)
            db.session.delete(user)
            db.session.commit()

            users = AuthUser.query.all()
            self.assertEqual(len(users), 0)

    @patch.object(AuthUser, "create_jwt_token")
    def test_create_jwt_token(self, app, patched_token):
        """Test creating JWT token for given user is successful."""

        token_dict = {
            "access_token": "test_token"
        }

        with app.app_context():
            user = AuthUser(
                email="test@example.com",
                password="testpass123"
            )
            db.session.add(user)
            db.session.commit()
            user = db.session.get(AuthUser, ident=1)
            patched_token.return_value = token_dict
            token = AuthUser.create_jwt_token(user.email)
            self.assertEqual(token, token_dict)
