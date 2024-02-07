from flask import Blueprint, jsonify, request
from app.controllers.interface import ClientInterface
from app.models.student_data_model import StudentDataModel
from app.database import db
from app.conf.constants import BASE_URL
from app.schemas.student_data_schema import StudentSchema


import json
import requests

student_data_blueprint = Blueprint("student_data", __name__)

@student_data_blueprint.route("/api/students", methods=["GET", "POST"]) #Where this is located
def student_data_list():
    if request.method == "GET":
        students = db.session.query(StudentDataModel).all() #Gets all the data inside the data model
        if len(students) <= 0:
            error_msg = "No results"
            return jsonify(msg=error_msg, status=200), 200 #Status 200 code means it is successful

        student_schema = StudentSchema(many=True) #copies the schema
        data = student_schema.dump(students) #Stores the data obtained into the schema

        return jsonify(data=data, status=200), 200
    else:
        data = request.json #getting the data from request in json format
        try:
            name = data["name"]
            nationality = data["nationality"]
            city = data["city"]
            lat = data["lat"]
            long = data["long"]
            gender = data["gender"]
            age = data["age"]
            english_grade = data["english_grade"]
            maths_grade = data["maths_grade"]
            sciences_grade = data["sciences_grade"]
            languages_grade = data["languages_grade"]

            new_student = StudentDataModel(name=name, nationality=nationality, city=city, lat=lat, long=long,
                                           gender=gender, age=age, english_grade=english_grade, maths_grade=maths_grade,
                                           sciences_grade=sciences_grade, languages_grade=languages_grade )

            db.session.add(new_student)

            db.session.commit()

            success_message = "New student has been created"

            return jsonify(msg=success_message, data=data, status_code=201), 201

        except:
            pass