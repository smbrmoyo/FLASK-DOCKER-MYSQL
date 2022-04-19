from typing import Dict
from flask_login import UserMixin

from app import db


class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(
        db.DateTime, nullable=False, default=db.func.current_timestamp()
    )
    

class UpdatableModel(BaseModel):
    __abstract__ = True
    updated_at = db.Column(db.DateTime, nullable=True)


class User(BaseModel, UserMixin):
    _tablename__ = "users"
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(64))

    def to_json(self) -> Dict:
        return {
            "id": self.id,
            "email": self.email,
            "username": self.username,
            "password": self.password,
            "createdAt": self.created_at,
        }


class Building(UpdatableModel):
    _tablename__ = "buildings"
    building_name = db.Column(db.String(255), nullable=False)
    geo_longitude = db.Column(db.Float, nullable=False)
    geo_latitude = db.Column(db.Float, nullable=False)
    sensor_readings = db.relationship("SensorReading", backref="building", lazy=True)

    def to_json(self) -> Dict:
        return {
            "id": self.id,
            "buildingName": self.building_name,
            "geoLongitude": self.geo_longitude,
            "geoLatitude": self.geo_latitude,
            "createdAt": self.created_at,
            "updatedAt": self.updated_at,
        }


class SensorReading(BaseModel):
    _tablename__ = "sensor_readings"
    building_id = db.Column(db.Integer, db.ForeignKey("building.id"), nullable=False)
    sensor_name = db.Column(db.String(255), nullable=False)
    sensor_value = db.Column(db.Float, nullable=False, default=0.0)

    def to_json(self) -> Dict:
        return {
            "id": self.id,
            "buildingId": self.building_id,
            "sensorName": self.sensor_name,
            "sensorValue": self.sensor_value,
            "createdAt": self.created_at,
        }
