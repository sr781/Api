from app.serializer import ma
from app.database import db
from app.server.api.models.address_model import Address
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class AddressSchema(SQLAlchemyAutoSchema):
    """Serializable schema for the Address model."""

    class Meta:
        model = Address
        fields = ("user_id", "street", "suite", "city", "zipcode", "lat", "long")
        include_fk = True
        sqla_session = db.session

    user_id = ma.auto_field()
