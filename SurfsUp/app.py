# Import the dependencies.
import numpy as np
import pandas as pd
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
@app.route("/")
def welcome():
    return (
        f"Available routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations/br/>"
        f"/api/v1.0/tobs/br/>"
        f"/api/v1.0/start/br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():

    #Convert the query results from your precipitaion analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.
    one_yr_earlier_dt = one_yr_earlier.strftime("%Y-%m-%d")

    prcp_data = session.query(Measurement.date,Measurement.prcp).\
    filter(Measurement.date > one_yr_earlier_dt).\
    order_by(Measurement.date).all()
      
    prcp_dict = {}
    for date, prcp in prcp_data:
        prcp_dict["date"] = date
        prcp_dict["prcp"] = prcp

    #Return the JSON represenatation of your dictionary
    return jsonify(prcp_dict)

    
@app.route("/api/v1.0/statioins")
def stations():

    #Return a JSON list of stations from the dataset
    results = session.query(Station.station).all()

    session.close()

@app.tobs("/api/v1.0/tobs")
def tobs():

    most_active_station_id  = most_active_station_id
    all_temperatures = []


    #Query the dates and temperature observations of the most-active station for the previous year of data
    data_from_last_year = session.query(Measurement.date, Measurement.tobs).filter(Measurement.station == most_active_station_id).filter(Measurement.date >= data_from_last_year).all()

    session.close()

    #Return a JSON list of temperature observations for the previous year.
    return jsonify(all_temperatures)


@app.route("/api/v1.0/<start>") 
@app.route("/api/v1.0/<start>/<end>")
def start_end_date(start, end):

    start_end_date_tobs_results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\ 
    filter(Measurement.date >= start).\
    filter(Measurement.date <= end).all()
    session.close()

    #Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
    start_end_tobs_date_values = []
    for min, avg, max in start_end_date_tobs_results:
        start_end_tobs_date_dict = {}
        start_end_tobs_date_dict["min_temp"] = min
        start_end_tobs_date_dict["avg_temp"] = avg
        start_end_tobs_date_dict["max_temp"] = max
        start_end_tobs_date_values(start_end_tobs_date_dict)

    return jsonify(start_end_tobs_date_values)


    #For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.
    results = session.query(func.min(Measurement.tobs),\
                            func.avg(Measurement.tobs), func.mac(Measurement.tobs)).\
                                 filter(Measurement.date >= start).all()
    session.close()
   

    #For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.
    results = session.query(func.min(Measurement.tobs),\
                            func.avg(Measurement.tobs), func.mac(Measurement.tobs)).\
                                 filter(Measurement.date >= start).filter(Measurement.date <= end date.all)()
    session.close()







   




        
    

#################################################

