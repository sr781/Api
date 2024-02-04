from app.server.api.models.address_model import Address
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class AddressSchema(SQLAlchemyAutoSchema):
    """Serializable schema for the Address model."""

    class Meta:
        model = Address  # We need to link our Address schema with our Address SQLAlchemy model.

        # Define the fields which will be included in the output when our model is serialized.
        fields = ("user_id", "street", "suite", "city", "zipcode", "lat", "long")


