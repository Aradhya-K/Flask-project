#import necessary modules
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from flask_marshmallow import Marshmallow

#initialize SQLAlchemy

db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    #create an instance of the flask application
    app = Flask(__name__)

    #load configuration from Config class
    app.config.from_object(Config)

    #initialize SQLAlchemy with the flask app3
    db.init_app(app)
    ma.init_app(app)

    #import and resistor the blueprint
    from .routes import main as main_blueprint
    app.resister_blueprint(main_blueprint)

    from .errors import errors as errors_blueprint
    app.resister_blueprint(errors_blueprint)

    return app