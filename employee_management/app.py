#import models
from flask import Flask
from model import db
from model import Employee
from config import Config
from flask_sqlalchemy import SQLAlchemy #type : ignore

#create an instance flask class
app = Flask(__name__)

#load the configuration settings from the config module
app.config.from_object('config.Config')

#create an instance of SQLAlchemy and bind it to the flask app\
db = SQLAlchemy(app)

from routes import *

#run the flask application in debug mode
if __name__ == '__main__':
    app.run(debug=True)