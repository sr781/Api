"""Use it to create the flask app itself"""


from flask import Flask
from .views.index import index_test_blueprint #imports the class "index_test_blueprint" to be created
from .serializer import ma
from .database import db
from .views.student_data import student_data_blueprint
from .views.address_data import address_data_blueprint
def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:admin@localhost/student_and_address_api" #Finds the
    #location of the schema on mysql
    ma.init_app(app) #for marshmallow to work
    db.init_app(app) #for SQLAlchemy to work

    with app.app_context():
        db.create_all() #All tables that have been defined are created
        db.session.commit()



    app.register_blueprint(index_test_blueprint) #For the index
    app.register_blueprint(student_data_blueprint)
    app.register_blueprint(address_data_blueprint)

    return app

