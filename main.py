import os

from flask_migrate import Migrate

from app import create_app, db
from app.models import Building, SensorReading
from config import DEFAULT_CONFIG

app = create_app(os.getenv("TARGET_ENVIRONMENT") or DEFAULT_CONFIG)
migrate = Migrate(app=app, db=db)

@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, Building=Building, SensorReading=SensorReading)

@app.cli.command()
def seed_db():
    import random 
    building_names = ["Pegasus", "Elixir", "Moon Tiger Enterprise"]
    sensor_names = ["temperature_sensor", "humidity_sensor", "light_sensor"]

    for name in building_names:
        buildig = Building(
            building_name=name,
            geo_longitude=random.random(),
            geo_latitude=random.random(),
        )

        db.session.add(buildig)
        db.session.commit()

    buildings = Building.query.all()
    for building in buildings:
        for _ in range(25):
            reading = SensorReading(
                building_id=building.id,
                sensor_name=sensor_names[random.randint(0,2)],
                sensor_value = random.random() * 10
            )

            db.session.add(reading)
    db.session.commit()

@app.cli.command()
def clear_db():
    db.session.query(SensorReading).delete()
    db.session.query(Building).delete()
