"""Create the structure for the student table"""
from app.database import db #importing the db instance from the database file to be able to work with SQLAlchemy
from app.models.address_data_model import AddressDataModel #Needed to make 'relationship' work?
class StudentDataModel(db.Model):

    """The code below is the data structure for one student """
    __tablename__ = "student_data" #Name of the table which will appear on MySQL

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    nationality = db.Column(db.String(50), nullable=True)
    city = db.Column(db.String(50), nullable=True)
    lat = db.Column(db.String(50), nullable=True)
    long = db.Column(db.String(50), nullable=True)
    gender = db.Column(db.String(20), nullable=True)
    age = db.Column(db.Integer, nullable=False) #Possibly float not whole number
    english_grade = db.Column(db.Integer, nullable=False)
    maths_grade = db.Column(db.Integer, nullable=False)
    sciences_grade = db.Column(db.Integer, nullable=False)
    languages_grade = db.Column(db.Integer, nullable=False)
    address_data_model = db.relationship("AddressDataModel", cascade="all, delete-orphan") #Relationship between
    # address_data_model by class
    # The child object which in this case is the "student_address_data" table will be deleted if the parent
    # "student_data" table which corresponds to the primary and foreign key is deleted

    def __init__(self, name, nationality, city, lat, long, gender, age, english_grade, maths_grade, sciences_grade,
                 languages_grade):
        self.name = name
        self.nationality = nationality
        self.city = city
        self.lat = lat
        self.long = long
        self.gender = gender
        self.age = age
        self.english_grade = english_grade
        self.maths_grade = maths_grade
        self.sciences_grade = sciences_grade
        self.languages_grade = languages_grade

    def __str__(self):
        return f"Student ID: {self.id} Name: {self.name} Age: {self.age}" #Returns this when called to make the output
        # more readble