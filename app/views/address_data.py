from flask import Blueprint, jsonify, request
from app.controllers.interface import ClientInterface
from app.database import db
from app.models.student_data_model import StudentDataModel #Used to find the data for the Address
from app.models.address_data_model import AddressDataModel
from app.schemas.address_data_schema import AddressSchema
address_data_blueprint = Blueprint("address_data", __name__)

@address_data_blueprint.route("/api/addresses", methods=["GET", "POST"])
def address_data_list():
    client_interface = ClientInterface("/addresses")

    if request.method == "GET":
        address = db.session.query(AddressDataModel).all()
        if len(address) <= 0:
            error_message = "No results in Addresses"
            return jsonify(msg=error_message, status=200), 200

        address_schema = AddressSchema(many=True) #Schema copied
        data = address_schema.dump(address) #Stores the data obtained into the schema
        return jsonify(data=data, status=200), 200

        #return jsonify(client_interface.get_list()) #Add len checker
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



            new_address_input = AddressDataModel(student_id=student.id, number=number, house_name=house_name, road=road,
                                              city=city, state=state, country=country, zipcode=zipcode)

            db.session.add(new_address_input) #Stages the code

            db.session.commit() #Commit will update the tables in mysql

            success_message = "New address data created for a student"
            return jsonify(data=data, msg=success_message, status=201), 201 #Sucess, with 201 indicating that a new
            #resource has been created
        except KeyError:
            error_message = "Please specify the fields for address"
            return jsonify(msg=error_message, status=400), 400 #Error on clients side