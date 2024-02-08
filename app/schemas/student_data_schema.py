from app.serializer import ma #Using marshmallow to convert data from Python to JSON for use in HTTP APIs
from app.models.student_data_model import StudentDataModel
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema #automatically generate fields so all you need are column names
from app.schemas.address_data_schema import AddressSchema
class StudentSchema(SQLAlchemyAutoSchema):

    class Meta:

        model = StudentDataModel #The StudentDataModel will be serialised

        #Fields generated with the student data model is serialised
        fields = ( "name", "nationality", "city", "lat", "long", "gender", "age", "english_grade", "maths_grade",
                  "sciences_grade", "languages_grade") #, "student_address_data")




    #student_data_sc = ma.Nested()