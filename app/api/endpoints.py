from flask import jsonify, flash, request, render_template, current_app, make_response, abort
from flask_login import login_required
import logging

from . import api
from .. import db
from ..models import Building, SensorReading
from ..forms import BuildingForm


@api.route("/")
@login_required
def index():
    
    info={
        "message": "Assesment test server is running",
        "author": "developer@dabbel.eu",
        "version": "0.0.1",
    }

    return render_template('index.html', info=info)
    

@api.route("/buildings")
@login_required
def get_buildings():
    # buildings = Building.query.filter_by(Building.building_name).first()
    if 'name' in request.args:
        name = request.args['name']
        building = [Building.query.filter_by(building_name=name).first()]
        return render_template('buildings.html', buildings=building)
    
    buildings = Building.query.all()
    return render_template('buildings.html', buildings=buildings)


@api.route("/create-building", methods=['GET', 'POST'])
@login_required
def create_building():

    form = BuildingForm()
    if form.validate_on_submit():
        try:
            building = Building(building_name=form.building_name.data, geo_latitude=form.geo_latitude.data,
            geo_longitude=form.geo_longitude.data)
            db.session.add(building)
            db.session.commit()
            return make_response(jsonify(building.to_json()))
        except:
            flash('There was an error creating the building', category='error')
            logging.error('There was an error creating the building')

    else:
        return render_template('create_building.html', form=form)



@api.route("/delete-building/<id>", methods=["POST", "GET"])
@login_required
def delete_building_id(id):

    building_to_delete = Building.query.get_or_404(id)

    if not building_to_delete:
        flash("This building does not exist.", category='error')
        logging.info('Requested building was not found')
        abort(404)

    else:
        try:
            db.session.delete(building_to_delete)
            db.session.commit()
            return make_response(jsonify(building_to_delete.to_json()))
        except:
            flash('There was an error deleting the building', category='error')
            logging.error('There was an error deleting the building')


@api.route("/update-building/<id>", methods=['GET', 'POST'])
@login_required
def update_building(id):

    building_to_update = Building.query.get(id)

    if not building_to_update:
            logging.error('Requested building was not found')
            abort(404)

    form = BuildingForm(obj=building_to_update)
    if form.validate_on_submit():
        building_to_update.building_name = form.building_name.data
        building_to_update.geo_longitude = form.geo_longitude.data
        building_to_update.geo_latitude = form.geo_latitude.data

        try:
            db.session.commit()
            return make_response(jsonify(building_to_update.to_json()))
        except:
            flash('There was an error creating the building', category='error')
            logging.error('There was an error creating the building')

    
    return render_template('update_building.html', form=form)

    


@api.route("/readings")
@login_required
def get_sensor_readings():

    if 'building' in request.args:
        param = request.args['building']
        building = Building.query.filter_by(building_name=param).first()

        if not building:
            logging.error('Requested building not found')
            abort(404)

        readings = SensorReading.query.filter_by(building_id=building.id).all()
        data = [r.to_json() for r in readings]

        return make_response(jsonify(readings=data))

    if 'sensor' in request.args:
        param = request.args['sensor']

        if not param:
            logging.error('Requested sensor not found')
            abort(404)

        readings = SensorReading.query.filter_by(sensor_name=param).all()
        data = [r.to_json() for r in readings]

        return make_response(jsonify(readings=data))

    readings = SensorReading.query.all()
    data = [r.to_json() for r in readings]

    return make_response(jsonify(readings=data))


@api.route("/metrics")
@login_required
def get_metrics():
    # readings = SensorReading.query.all()
    # data = [r.to_json() for r in readings]

    return "hello"
