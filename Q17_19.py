from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify

engine = create_engine("sqlite:///titanic.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

Passenger = Base.classes.passenger

app = Flask(__name__)

@app.route("/")
def welcome():
   """List all available api routes."""
   return (
       f"Available Routes:<br/>"
       f"/api/v1.0/names<br/>"
       f"/api/v1.0/passengers"
   )

### Create an endpoint for names ###

if __name__ == '__main__':
   app.run(debug=True)