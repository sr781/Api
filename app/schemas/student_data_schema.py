from app.serializer import ma #Using marshmallow to convert data from Python to JSON for use in HTTP APIs
from app.models.student_data_model import StudentDataModel
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema #automatically generate fields so all you need are column names

class StudentSchema(SQLAlchemyAutoSchema):

    class Meta:

        model = StudentDataModel

        fields = ("id", "name", "nationality", "city", "lat", "long", "gender", "age", "english_grade", "maths_grade",
                  "sciences_grade", "languages_grade", )


    student_data_sc = ma.Nested()