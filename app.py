
#practice code from module. double asterisk lines are code that has been commented out.
##from flask import Flask
##app = Flask(__name__)
##@app.route('/')
##def hello_world():
##    return 'Hello world'


##C:\Users\travi\OneDrive\Desktop\Data\Module-9\Surfs_Up>set Flask_App=app.py

##C:\Users\travi\OneDrive\Desktop\Data\Module-9\Surfs_Up>flask run
## * Serving Flask app 'app.py'
## * Debug mode: off
##WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
## * Running on http://127.0.0.1:5000


#Import dependencies
import datetime as dt
import numpy as np
import pandas as pd
#Import sqalchemy dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
#import flask dependencies
from flask import Flask, jsonify
#create an engine that allows access to sqlite file
engine = create_engine("sqlite:///hawaii.sqlite")
#reflect database into classes
Base = automap_base()
Base.prepare(engine, reflect=True)
#create variable to refer to each class
Measurement = Base.classes.measurement
Station = Base.classes.station
#create variable for session link
session = Session(engine)
#create flask app
app = Flask(__name__)
#import app

##print("example __name__ = %s", __name__)

##if __name__ == "__main__":
##    print("example is being run directly.")
##else:
##    print("example is being imported")

@app.route("/")
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')