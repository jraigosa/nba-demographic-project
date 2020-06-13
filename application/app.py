#Import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy import and_, or_

#Import Flask
from flask import Flask, jsonify

#Import NumPy
import numpy as np

#Import Mean
from scipy import mean

#Database Setup
engine = create_engine("sqlite:///../Resources/sqlite/nbaData.sqlite")

#Reflect existing database
Base = automap_base()

#Reflect tables
Base.prepare(engine, reflect=True)

#Save references to the tables
Player = Base.classes.Player
Race = Base.classes.Race
Counties = Base.classes.Counties
Poverty = Base.classes.Poverty

#Flask Setup
app = Flask(__name__)

@app.route("/")
def index():


   
@app.route("/race")
def race():

@app.route("/economic")
def economic():
    

if __name__ == "__main__":
    app.run(debug=True)
