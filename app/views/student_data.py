from flask import Blueprint, jsonify, request
from app.controllers.interface import ClientInterface
from app.models.student_data_model import StudentDataModel
from app.database import db
from app.conf.constants import BASE_URL
from app.schemas.student_data_schema import StudentSchema

import json
import requests

student_data_blueprint = Blueprint("student_data", __name__)

@student_data_blueprint.route("/api/students", methods=["GET", "POST"])
def student_data_list():
    if request.method == "GET":
        pass

    else:
        data = request.json
        try:
            id = data["id"]
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

            new_student = StudentDataModel(id=id, name=name, nationality=nationality, city=city, lat=lat, long=long,
                                           gender=gender, age=age, english_grade=english_grade, maths_grade=maths_grade,
                                           sciences_grade=sciences_grade, languages_grade=languages_grade )

            #db.session.add(new_student)

            #db.session.commit()

            success_message = "New student has been created"

            return jsonify(msg=success_message, data=data, status_code=201), 201

        except:
            pass