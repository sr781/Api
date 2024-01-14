from app.serializer import ma
from app.server.api.models.user_model import User
from app.server.api.models.schemas.address_schema import AddressSchema


class UserSchema(ma.SQLAlchemySchema):
    """Serializable schema for the User object."""

    class Meta:
        model = User
        fields = ("id", "name", "username", "email", "phone", "addresses")

    addresses = ma.Nested(AddressSchema, many=True)
