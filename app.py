import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Passenger = Base.classes.passenger

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List of all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0<start>/<end>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return percipitation based on date"""
    # Query all passengers
    results = session.query(Measurement.date, Measurement.prcp).all()

    session.close()

    # Create a dictionary from the row data and append precipitation to date
    all_prcp = []
    for prcp in date:
        prcp_dict = {}
        prcp_dict["date"] = prcp
        all_prcp.append(prcp_dict)

    return jsonify(all_prcp)


@app.route("/api/v1.0/stations")
def station():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return percipitation based on date"""
    # Query all passengers
    results = session.query(Measurement.station).all()

    session.close()

    # Convert list of tuples into normal list
    all_station = list(np.ravel(results))

    return jsonify(all_station)

@app.route("/api/v1.0/tobs")
def temperature():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return temperature based on date"""
    # Query all passengers
    results = session.query(Measurement.date, Measurement.tobs).all()

    session.close()

    # Create a dictionary from the row data and append temperature to date
    all_tobs = []
    for tobs in date:
        temp_dict = {}
        temp_dict["date"] = tobs
        all_tobs.append(temp_dict)

    return jsonify(all_tobs)

@app.route("/api/v1.0/start")
def start():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return minumum, maximum and average temperature based on all dates greater than start date"""
    # Query all passengers
    results = session.query(Measurement.date, Measurement.tobs).all()

    session.close()

    # Create a dictionary from the row data and append temperatures for dates greater than start date
    Dates = []
    for date in Dates:
        sel = [Measurement.date, 
            func.min(Measurement.tobs), 
            func.max(Measurement.tobs), 
            func.avg(Measurement.tobs)]
        date_temps = session.query(*sel).\
        filter(Measurement.date > 'date').all()
        Dates.append(date_temps)
    
    return jsonify(Dates)

@app.route("/api/v1.0/<start>")
def start():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return minumum, maximum and average temperature based on all dates greater than start date"""
    # Query all passengers
    results = session.query(Measurement.date, Measurement.tobs).all()

    session.close()

    # Create a dictionary from the row data and append temperatures for dates greater than start date
    Dates = []
    for date in Dates:
        sel = [Measurement.date, 
            func.min(Measurement.tobs), 
            func.max(Measurement.tobs), 
            func.avg(Measurement.tobs)]
        date_temps = session.query(*sel).\
        filter(Measurement.date > 'date').all()
        Dates.append(date_temps)
    
    return jsonify(Dates)

@app.route("/api/v1.0/<start>/<end>")
def start():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return minumum, maximum and average temperature based on all dates between start date and end date"""
    # Query all passengers
    results = session.query(Measurement.date, Measurement.tobs).all()

    session.close()

    # Create a dictionary from the row data and append temperatures for dates greater than start date
    start_date = []
    end_date = []
    query_period = end_date - start_date
    query_date = query_period[]
    for date in query_date:
        sel = [Measurement.date, 
            func.min(Measurement.tobs), 
            func.max(Measurement.tobs), 
            func.avg(Measurement.tobs)]
        end_temps = session.query(*sel).\
        filter(Measurement.date == 'query_period').all()
        query_date.append(end_temps)
    
    return jsonify(query_date)


if __name__ == '__main__':
    app.run(debug=True)