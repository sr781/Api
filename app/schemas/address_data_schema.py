from app.models.address_data_model import AddressDataModel
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
#Take data and turn into json

class AddressSchema(SQLAlchemyAutoSchema):

    class Meta:
        model = AddressDataModel
        fields = ("id", "student_id", "number", "house_name", "road", "city", "state", "country", "zipcode")