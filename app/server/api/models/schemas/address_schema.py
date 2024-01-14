from app.serializer import ma
from app.server.api.models.address_model import Address


class AddressSchema(ma.SQLAlchemySchema):
    """Serializable schema for the Address model."""

    class Meta:
        model = Address
        fields = ("street", "suite", "city", "zipcode", "lat", "long")
        include_fk = True
