from flask import Blueprint, jsonify, request
from app.database import db
from app.models.student_data_model import StudentDataModel #Used to find the data for the Address
from app.models.address_data_model import AddressDataModel
from app.schemas.address_data_schema import AddressSchema
address_data_blueprint = Blueprint("address_data", __name__)

"""Perform functions to get, update, delete or view data for the address data"""
@address_data_blueprint.route("/api/addresses", methods=["GET", "POST"])
def address_data_list():

    if request.method == "GET":
        address = db.session.query(AddressDataModel).all()
        if len(address) <= 0:
            error_message = "No results in Addresses"
            return jsonify(msg=error_message, status=200), 200

        address_schema = AddressSchema(many=True) #Schema copied
        data = address_schema.dump(address) #Stores the data obtained into the schema
        return jsonify(data=data, status=200), 200

    else:
        data = request.json #In the variable data, the request method is used to obtain data (in json format)
        try:
            fk_student_id = data["student_id"] #"student_id" is the foreign key of "id" from the student table
            student = db.session.query(StudentDataModel).filter_by(id=fk_student_id).first() #Obtains first result
            if not student:
                error_message = "Student not found"
                return jsonify(msg=error_message, status=400), 400 #Bad request from client side

            #student_id = data["student_id"]
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
            error_message = ("Please specify the fields, <student_id>, <number>, <house_name>, <road>, <city>, <state>"
                             "<country>, <zipcode> for address")
            return jsonify(msg=error_message, status=400), 400 #Error on clients side


@address_data_blueprint.route("/api/addresses/<int:address_id>", methods=["GET"])
def get_single_address(address_id):
    address = db.session.query(AddressDataModel).filter_by(id=address_id).first() #Looks in the column 'id' for the given
    # address_id number and selects the first result which is assigned to the variable, "address". Obtains
    #the data in the row

    if not address: #if the table does not find the record with the corresponding id, this will run
        error_message = f"Address with the id {address_id} was not found "
        return jsonify(msg=error_message, status=200), 200 #Indicates request was successful (works fine, data was just
        # not found)

    address_data_schema = AddressSchema(many=False)
    data = address_data_schema.dump(address) #Result from the first row is taken and added to the schema (does not update)

    return jsonify(data=data, status=200), 200 #Indicates success (not 201 because nothing is changed)

@address_data_blueprint.route("/api/addresses/<int:address_id>", methods=["PATCH"])#To partially or fully update
# a record based on the id of the address
def patch_single_address(address_id):
    data = request.json #Data sent from postman assigned to the variable 'data'

    address = db.session.query(AddressDataModel).filter_by(id=address_id).first() #As explained in the "GET" method
    if not address: #if the table does not find the record with the corresponding id, this will run
        error_message = f"Address with the id {address_id} was not found "
        return jsonify(msg=error_message, status=200), 200

    try:
        for key, value in data.items():
            if not hasattr(AddressDataModel, key): #checks if the key value pairs in "data" has the attributes from the
                #AddressDataModel object
                raise ValueError
            else:
                setattr(address, key, value)
                db.session.commit() #The commit function will update the table in sql


        address = db.session.query(AddressDataModel).filter_by(id=address_id).first()
        address_schema = AddressSchema(many=False)
        data = address_schema.dump(address)

        success_message = f"Address with ID {address.id} updated"
        return jsonify(msg=success_message, data=data, status=200), 200 #Sucess message, no data was created

    except ValueError:
        error_message = "Error referencing columns, <student_id>, <number>, <house_name>, <road>, <city>, <state>"
        "<country>, <zipcode> for address"
        return jsonify(msg=error_message, status=400), 400 #Bad request