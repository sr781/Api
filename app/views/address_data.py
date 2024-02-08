from flask import Blueprint, jsonify, request
from app.controllers.interface import ClientInterface
from app.database import db
from app.models.student_data_model import StudentDataModel #Used to find the data for the Address
from app.models.address_data_model import AddressDataModel

#address_data_blueprint = Blueprint("address_data", __name__)

#@address_data_blueprint.route("/api/addresses", methods=["GET", "POST"])
#def address_data_list()

