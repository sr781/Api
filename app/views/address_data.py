from flask import Blueprint, jsonify, request
from app.controllers.interface import ClientInterface
from app.database import db
from app.models.student_data_model import StudentDataModel #Used to find the data for the Address
from app.models.address_data_model import AddressDataModel



address_data_blueprint = Blueprint("address_data", __name__)

@address_data_blueprint.route("/api/addresses", methods=["GET", "POST"])
def address_data_list():
    client_interface = ClientInterface("/addresses")

    if request.method == "GET":
        return jsonify(client_interface.get_list()) #Add len checker
    else:
        data = request.json #In the variable data, the request method is used to obtain data (in json format)
        try:
            fk_student_id = data["student_id"] #"student_id" is the foreign key of "id" from the student table
            student = db.session.query(StudentDataModel).filter_by(id=fk_student_id).first() #Obtains first result
            if not student:
                error_message = "Student not found"
                return jsonify(msg=error_message, status=400), 400 #Bad request from client side

            student_id = data["student_id"]
            number = data["number"]
            house_name = data["house_name"]
            road = data["road"]
            city = data["city"]
            state = data["state"]
            country = data["country"]
            zipcode = data["zipcode"]

            new_address_input = AddressDataModel

