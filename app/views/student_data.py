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
    if request.method == "GET": #To recieve all data
        students = db.session.query(StudentDataModel).all() #Gets all the data inside the data model
        if len(students) <= 0:
            error_msg = "No results" #If there is no data, this message will show up on the return
            return jsonify(msg=error_msg, status=200), 200 #Status 200 code means it is successful

        student_schema = StudentSchema(many=True) #copies the schema
        data = student_schema.dump(students) #Stores the data obtained into the schema

        return jsonify(data=data, status=200), 200 #request was sucessful
    else:
        data = request.json #Data sent from postman assigned to the variable 'data'
        try:
            #Key value pairs
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

            #create a new instance of student, passing on the required fields
            new_student = StudentDataModel(name=name, nationality=nationality, city=city, lat=lat, long=long,
                                           gender=gender, age=age, english_grade=english_grade, maths_grade=maths_grade,
                                           sciences_grade=sciences_grade, languages_grade=languages_grade )

            db.session.add(new_student) #updates the database with the new student

            db.session.commit() #This will save the data for the new student

            success_message = "New student has been created"

            return jsonify(msg=success_message, data=data, status_code=201), 201 #Message 201 indicates success and the
            # creation of a new resource

        except KeyError: #Error handling. A key error is just there to check if the required columns have their required
            #values
            error_message = "Please check to make sure all the data has been added and POST again"
            return jsonify(msg=error_message, status_code=400) #A 400 Error is due to something on the client side

@student_data_blueprint.route("/api/students/<int:student_id>", methods=["GET"]) #To get one row based on the
#student id
def get_single_user(student_id):
    student = db.session.query(StudentDataModel).filter_by(id=student_id).first() #Looks in the column 'id' for the given
            # student_id number and selects the first result which is assigned to the variable, "student". Obtains
            #the data in the row

    if not student_id: #if the table does not find the record with the corresponding id, this will run
        error_message= f"Student with the id {student_id} was not found "
        return jsonify(msg=error_message, status=200), 200 #Indicates request was successful (works fine, data was just
        # not found)

    student_data_schema = StudentSchema(many=False)
    data = student_data_schema.dump(student) #Result from the first row is taken and added to the schema (does not update)

    return jsonify(data=data, status=200), 200 #Indicates success (not 201 because nothing is changed)

@student_data_blueprint.route("/api/students/<int:student_id>", methods=["PATCH"]) #To partially or fully update
# a record based on the id of the student
def patch_single_user(student_id):
    data = request.json #Data sent from postman assigned to the variable 'data'

    student = db.session.query(StudentDataModel).filter_by(id=student_id).first() #As explained in the "GET" method
    if not student_id: #if the table does not find the record with the corresponding id, this will run
        error_message= f"Student with the id {student_id} was not found "
        return jsonify(msg=error_message, status=200), 200

    try:
        for key, value in data.items():
            if not hasattr(StudentDataModel, key): #checks if the key value pairs in "data" has the attributes from the
                #StudentDataModel object
                raise ValueError
            else:
                setattr(student, key, value)
                db.session.commit() #The commit function will update the table in sql


        student = db.session.query(StudentDataModel).filter_by(id=student_id).first()
        student_schema = StudentSchema(many=False)
        data = student_schema.dump(student)

        success_message = f"Student with ID {student.id} updated"
        return jsonify(msg=success_message, data=data, status=200), 200 #Sucess message, no data was created

    except ValueError:
        error_message = "Error referencing columns with provided keys"
        return jsonify(msg=error_message, status=400), 400 #Bad request


# @student_data_blueprint.route("/api/students/<int: student_id>", methods=["DELETE"]) #To delete a user
# def delete_single_user(student_id):
#     student = db.session.query(StudentDataModel).filter_by(id=student_id).first() #Looks in the column 'id' for the given
#     # student_id number and selects the first result which is assigned to the variable, "student". Obtains
#     #the data in the row
#
#     if not student_id: #if the table does not find the record with the corresponding id, this will run
#         error_message= f"Student with the id {student_id} was not found "
#         return jsonify(msg=error_message, status=200), 200 #Indicates request was successful (works fine, data was just
#         # not found)
#
#
#
#
#
#
#
#     db.session.delete(new_student) #updates the database with the new student
#
#     db.session.commit() #This will save the data for the new student
#     data = student_schema.dump(student)