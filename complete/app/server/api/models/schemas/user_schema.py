from app.database import db
from app.serializer import ma
from app.server.api.models.user_model import User
from app.server.api.models.address_model import Address
from app.server.api.models.schemas.address_schema import AddressSchema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy import fields
from app.server.api.models.base import DBInterface


class UserSchema(SQLAlchemyAutoSchema):
    """Serializable schema for the User object."""

    class Meta:
        model = User
        fields = ("id", "name", "username", "email", "phone", "addresses")
        include_relationships = True
        load_instance = True
        sqla_session = db.session

    addresses = ma.Nested(AddressSchema, many=True, dump_only=True)
    id = ma.Integer(dump_only=True)
