"""Create the structure for the address table"""
from app.database import db #importing the db instance from the database file to be able to work with SQLAlchemy

class AddressDataModel(db.Model): #The class inherits from db.Model where db is SQLAlchemy()
    """The code below is the data structure for the address of one student """
    __tablename__ = "student_address_data" #Name of the table which will appear on MySQL

    id = db.Column(db.Integer, primary_key=True, autoincrement=True) #Not the same as id for the student_data table
    student_id = db.Column(db.Integer, db.ForeignKey("student_data.id"), nullable=False) #This links the two tables
    # together. The 'id' column from the "student_data" table to the "student_id" column of this table
    number = db.Column(db.Integer, nullable=False)
    house_name = db.Column(db.String(50), nullable=False)
    road = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    zipcode = db.Column(db.String(50), nullable=False)
    student_data_model = db.relationship("StudentDataModel", backref="address_data_model")

    def __init__(self, student_id, number, house_name, road, city, state, country, zipcode):
        self.student_id = student_id
        self.number = number
        self.house_name = house_name
        self.road = road
        self.city = city
        self.state = state
        self.country = country
        self.zipcode = zipcode

    def __str__(self):
        return f"Address id {self.id} Student id {self.student_id} House name {self.house_name}" #Returns this when called to make the output more readble

