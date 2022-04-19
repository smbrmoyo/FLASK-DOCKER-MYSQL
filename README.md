## Introduction
We hope that this starter code gives you the opportunity to shine and show off your strengths.

A series of tasks have been laid out to grant you the opportunity to make minimal changes or go above and beyond to show off the extent of your skills in a given area : Software Engineering, Site Reliability Engineering, DevOps, UI, API, Security or Database skills.

Of the tasks under the categories you find below, we would like you to choose 3-4 to work on (at least attempt the Software Engineering, DevOps, and Security categories). We would rather you focus on demonstrating a few high quality skills or solutions over completing a large number of the tasks below.

Push all your solutions to a feature branch after your own name. For example, if your name is `Edward Pie`, push your changes to a branch named `edward-pie-assessment`.

## Instructions to get started
1. Run `python3 -m venv env` to create a virtual environment.
2. Run `source env/bin/activate` to activate the virtual environment.
3. Run `pip3 install -r requirements.txt` to install all dependencies.
4. Run `export FLASK_APP=main.py`.
5. Run `flask db init` to initialize the database setup.
6. Run `flask db migrate -m "some descriptive message"` to create the migrations directory. Do this also whenever you modify the models.
7. Run `flask db upgrade` to create tables in the database. Do this also whenever you modify the models.
8. Run `flask seed-db` to seed the database with fake data.
9. Finally, run `flask run` and point your browser to [http://localhost:5000/api](http://localhost:5000/api). If everything worked fine, you should see a JSON description of the server.

## Clearing and re-seeding the database
You might want to clear the database and re-seed it during development. In that case run `flask clear-db` to clear all tables, and run `flask seed-db` to seed the database with fake data again.

## Special instruction
Please push your migrations directory to your branch when submitting for review.

## Challenges
There is no one right answer. Prefer high quality code and applying your knowledge of best practices over completing more tasks.

### Category: Software Engineering
1. Modify the `/buildings` endpoint so that the API response can be filtered by building name using a `query parameter`.
2. Add endpoints to support the creation, updating, and deletion of buildings data. Where appropriate, the endpoint must accept JSON payloads and all endpoints must return JSON responses.
3. Modify the `/readings` endpoint to support filtering of response by `building name` and/or `sensor name` through the use of `query parameters`.
4. Add Cross Origin Resource Sharing (CORS) support to this application.
5. Add some unit tests to validate the core functionalities of this service.
6. As it stands now, if I make a request to [http://locahost:5000/api/fakeurl](http://locahost:5000/api/fakeurl) a generic `Not Found` error will be shown. Handle this and let all such requests return a JSON of the form `{"msg": "The requested resouce is not found."}`
7. Add a logger and log useful information where appropriate.
8. What would you have done differently if the entire source code had been your project to start with?


### Category: DevOps
1. `Dockerize` this application and change the backing database from SQLite to either `MySQL or Postgres`. Your chosen database must already be run as a docker container.
2. In your containers, make sure that the service run with the `gunicorn` server using `production configs`.
3. Explain to us how you would scale this service to allow for more traffic/ users /availability.

### Category: UI
1. Create a UI with tabs to show line plots for all the various sensors in the database. This means, fetch sensor readings from the `/readings` endpoints and show line graphs for the `temperature_sensor`, `humidity_sensor`, and `light_sensor` values chronologically.

### Category: Security
1. Make the API endpoints more secure by implementing your favorite `API authentication method`.
2. Explain why you chose your particular API security strategy and mention other approaches you could have taken.

### Category: Site Reliability Engineering
1. Make this service provide a `/metrics` endpoint to enable insights into the application's usage and performance.
2. Explain to us the relationship between development and operation and how this is made better in SRE.

Good luck!!!
