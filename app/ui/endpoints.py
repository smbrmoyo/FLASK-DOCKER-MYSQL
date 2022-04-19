from flask import render_template
from flask_login import login_required

from . import ui
from ..api import endpoints
from ..models import SensorReading, Building

@ui.route("/")
@login_required
def index():
    return render_template('index.html')

# Couldn't fetch the data from the readings endpoint
# I think the problem was with the authentication
# My response alaways was the script from the login page
# Here is an example of how I would have done it
"""
def get_values(sensorname):
    BASE = "http://127.0.0.1:5000/api/readings?sensor="
    json_url = requests.get(BASE + sensorname)
    data = json.loads(json_url.text.decode("utf-8"))
    values = []
    for element in data:
        values.append(element["sensorValue"])

    return values
"""


@ui.route("/light")
@login_required
def light():
    data = SensorReading.query.filter_by(sensor_name="light_sensor").all()
    values = []
    for datum in data:
        values.append(datum.sensor_value)

    labels = []
    for datum in data:
        labels.append(datum.id)

    return render_template('light.html', values=values, labels=labels)

@ui.route("/humidity")
@login_required
def humidity():
    data = SensorReading.query.filter_by(sensor_name="humidity_sensor").all()
    values = []
    for datum in data:
        values.append(datum.sensor_value)

    labels =[]
    for datum in data:
        labels.append(datum.id)

    return render_template('humidity.html', values=values, labels=labels)

@ui.route("/temperature")
@login_required
def temperature():
    data = SensorReading.query.filter_by(sensor_name="temperature_sensor").all()
    values = []
    for datum in data:
        values.append(datum.sensor_value)

    labels = []
    for datum in data:
        labels.append(datum.id)

    return render_template('temperature.html', values=values, labels=labels) 