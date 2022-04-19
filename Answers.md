### Category: Software Engineering

1. Modified the /buildings endpoint to filter by building_name.
2. Added endpoints to support CRUD operations.
3. Modified the /readings endpoint to filter by building_name and sensor_name.
4. Added CORS support to this application.
5. Added some unit testing.
6. Handled `Not Found` error.
7. Added logger. Mostly by errors. By expected response added flash messages for better UX.
8. Honestly, not much. I think simplicity is necessary when it comes to data manipulation.

### Category: DevOps

1. `Dockerized` this application and changed the backing database from SQLite to `MySQL`. MySQL is running as docker container
2. Somehow I couldn't get the `gunicorn` server to run. I thought the problem came from my computer but it seems I just can't access the app instance. I would be grateful if you could tell me what went wrong there. Nevertheless, the app is able to run using `production configs`, even without `gunicorn`.
3. In terms of scaling, the first thing that comes to mind is `Pagination`. We could limit the maxLength of various responses, and request them as users go along. Secondly, a caching system, by which we could store frequently requested data locally. That could help limit the amount of requests made to the server.

### Category: UI

1. Created a basic UI to plot the different sensor values. I couldn't fetch the data from the `/readings` endpoint directly. I thought my logic was right, but I couldn't get it to work.

### Category: Security

1. Implemented authentication using `flask_login`. Implemented users' authentication with sign up and sign in. Secured the different endpoints by requiring users to be logged in.
2. I chose `flask_login` for the simplicity and the compatibility. Theoretically, any other third-party library could have been used. Or even an implementation from scratch. And even using `flask_login`, I could've implemented a `JWT` logic with an expiring token and could have stored it locally, to allow a `Remember me` option to the login.

### Category: Site Reliability Engineering

1. I did not touch this part at all due to lack of time. I found a library called `prometheus-client` that was pretty well suited for the task. It allowed to count event and/or jobs, measure latency and build histogramms. I guess I could have added a counter to each endpoint to track the number of occurrences and measured the latency of each request.

THANK YOU FOR THE OPPORTUNITY!!!
