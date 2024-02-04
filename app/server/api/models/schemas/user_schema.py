from app.serializer import ma
from app.server.api.models.user_model import User
from app.server.api.models.schemas.address_schema import AddressSchema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class UserSchema(SQLAlchemyAutoSchema):
    """Serializable schema for the User object."""

    class Meta:
        model = User  # We need to link our UserSchema with our User SQLAlchemy model.

        # Define the fields which will be in the output when our User model is serialized.
        fields = ("id", "name", "username", "email", "phone", "addresses")

    # Define an extra nested field to contain any addresses associated with a user.
    # Note the many=True flag. This indicates that a user could have multiple addresses,
    # and each address should be stored in an array.
    addresses = ma.Nested(AddressSchema, many=True, dump_only=True)


