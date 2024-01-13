from app.tests.base import BaseTestCase
from app.tests.api_tests.helpers import create_user, create_address
from app.server.api.models.address_model import Address
from app.server.api.models.user_model import User
from app.server.api.models.base import DBInterface

from app.database import db


class AddressModelTests(BaseTestCase):
    """
    Test integration of Address model in Database

    Methods:
        test_create_address - Test address created successfully.
        test_update_address - Test address updated successfully.
        test_delete_address - Test address deleted successfully.
        test_address_assigned_to_expected_user - Test address bears relationship with expected user only.
        test_address_cascade_on_user_delete - Test address deleted when related user removed from DB.
    """

    def test_create_address(self, app):
        """Test creating an address"""

        with app.app_context():
            user = create_user()

            interface = DBInterface(db.session, user)
            interface.add_to_db()

            user = User.query.filter_by(id=1).first()

            address = create_address(user.id)
            interface = DBInterface(db.session, address)
            interface.add_to_db()

            addresses = Address.query.all()
            self.assertEqual(len(addresses), 1)
            self.assertEqual(addresses[0].street, "Test Street")
            self.assertEqual(addresses[0].suite, "Test Suite")
            self.assertEqual(addresses[0].city, "Test City")
            self.assertEqual(addresses[0].zipcode, "T35TZP")
            self.assertEqual(addresses[0].lat, "-3.01244")
            self.assertEqual(addresses[0].long, "24.34234")

    def test_update_address(self, app):
        """Test updating an address"""

        with app.app_context():
            user = create_user()
            interface = DBInterface(db.session, user)
            interface.add_to_db()

            user_with_address = User.query.filter_by(id=1).first()
            address = create_address(user_with_address.id)
            interface = DBInterface(db.session, address)
            interface.add_to_db()

            address_to_update = Address.query.filter_by(user_id=user.id).first()

            update_dict = {
                "street": "New Street",
                "city": "New City",
                "suite": "New Suite",
                "lat": "-3.1000"
            }

            address_to_update = DBInterface.get_object(Address, id=address_to_update.id)
            interface = DBInterface(db.session, address_to_update)
            interface.update_object(update_dict)

            updated_address = Address.query.filter_by(user_id=user.id).first()

            # Street, Suite, City updated only.
            self.assertEqual(updated_address.street, "New Street")
            self.assertEqual(updated_address.suite, "New Suite")
            self.assertEqual(updated_address.city, "New City")
            self.assertEqual(updated_address.zipcode, "T35TZP")
            self.assertEqual(updated_address.lat, "-3.1000")
            self.assertEqual(updated_address.long, "24.34234")

    def test_delete_address(self, app):
        """Test deleting an address."""

        with app.app_context():
            user = create_user()
            interface = DBInterface(db.session, user)
            interface.add_to_db()

            user_with_address = User.query.filter_by(id=1).first()
            address = create_address(user_with_address.id)
            interface = DBInterface(db.session, address)
            interface.add_to_db()

            address_to_delete = DBInterface.get_object(Address, id=address.id)
            interface = DBInterface(db.session, address_to_delete)
            interface.remove_from_db()

            addresses = Address.query.all()
            self.assertEqual(len(addresses), 0)

    def test_address_assigned_to_user(self, app):
        """Test that an address is able to be retrieved using the associated user's ID."""

        with app.app_context():
            user = create_user()
            interface = DBInterface(db.session, user)
            interface.add_to_db()
            user_with_address = User.query.filter_by(id=1).first()

            address = create_address(user_with_address.id)
            interface = DBInterface(db.session, address)
            interface.add_to_db()

            user_address = Address.query.filter_by(user_id=user.id).first()
            self.assertEqual(user_address.user_id, user.id)

    def test_address_cascade_on_user_delete(self, app):
        """Test that an address is able to be retrieved using the associated user's ID."""

        with app.app_context():
            user = create_user()
            interface = DBInterface(db.session, user)
            interface.add_to_db()

            user_with_address = User.query.filter_by(id=1).first()

            address = create_address(user_with_address.id)
            interface = DBInterface(db.session, address)
            interface.add_to_db()

            address_list = Address.query.all()
            self.assertEqual(len(address_list), 1)

            user_to_remove = DBInterface.get_object(User, id=user.id)
            interface = DBInterface(db.session, user_to_remove)
            interface.remove_from_db()

            new_address_list = Address.query.all()
            self.assertEqual(len(new_address_list), 0)

    def test_address_delete(self, app):
        """Test address is deleted from DB successfully."""

        with app.app_context():
            user = create_user()
            interface = DBInterface(db.session, user)
            interface.add_to_db()
            user_with_address = User.query.filter_by(id=1).first()

            address = create_address(user_with_address.id)
            interface = DBInterface(db.session, address)
            interface.add_to_db()

            address_list = Address.query.all()
            self.assertEqual(len(address_list), 1)

            address_to_delete = DBInterface.get_object(Address, id=address.id)
            interface = DBInterface(db.session, address_to_delete)
            interface.remove_from_db()

            empty_address_list = Address.query.all()
            self.assertEqual(len(empty_address_list), 0)
