# Phase 2: Create a Microservice

In this phase, you'll create a microservice with Flask and Postgres. 
Navigate to the `team_omega` folder in the skeleton and begin here by 
running `pipenv install` to create a virtual environment and install the
dependencies in the provided Pipfile. Be sure to create a `.env` file that 
mirrors the `.env.example` provided, specifying how you will connect to a 
database.

### Set up and seed the database
Let's start by creating a database and database user.

```sql
CREATE USER ratings_user WITH CREATEDB PASSWORD 'password';
CREATE DATABASE ratings WITH OWNER ratings_user;
```

Next, upgrade your database to create the book_ratings table. The migration
file is provided in the starter. All you need to do is run:

```bash
pipenv run flask db upgrade
```

Take a moment to check that your migrations were successful by viewing the
`alembic_version` and `book_ratings` tables in your `ratings` database.

Finally, seed your database using the provided `database.py` file:
```bash
pipenv run python database.py
```

### Test the Flask app

Start the Flask application server:

```bash
pipenv run flask run
```

Now you can visit the endpoint with your browser at
http://localhost:5000/ratings/1 or send a GET request with Postman to check if
your route is successfully fetching and rendering database ratings! Your JSON
response should look something like this:

```json
{
  "average": 7.67,
  "ratings": [
    {
      "value": 10
    },
    {
      "value": 8
    },
    {
      "value": 5
    }
  ]
}
```

Test a POST request to
`http://localhost:5000/ratings/1?value=8&email=ryan@email.com`. Notice the
`value` and `email` parameters listed in the URL. You should have received a
JSON response that looks something like this:

```json
{
  "book_id": 1,
  "email": "ryan@email.com",
  "id": 7,
  "value": 8
}
```

Now try to send another POST request with the same email:
`http://localhost:5000/ratings/1?value=1&email=ryan@email.com`. You should have
received the response `'Each user can only submit one rating per book.'`.


### Create the Dockerfile

Now that you've tested the Flask app, it's time to dockerize the microservice! 
You'll dockerize the Flask/Postgres microservice in a very similar way to how you 
dockerized the Express/Postgres application. You can even begin by copying over 
the Dockerfile and _docker-compose.yml_ file from your Express app. 
Let's begin by working off of the Dockerfile that creates your custom Node image.

**Dockerfile**

```
FROM node:12-alpine

WORKDIR /app

EXPOSE 8080
```

Have the Dockerfile for your Flask application use the `python` image with a tag
of `3.9-slim`. Then, update the exposed port to `5000`. Take a moment to create
a `requirements.txt` file based on the current dependencies in your `Pipfile`.
You can do this by running `pipenv run pip freeze > requirements.txt`. This will
automatically generate a `requirements.txt` file that lists all the installed
dependencies, along with their current version. Now add a `COPY` statement in 
your Dockerfile to copy the `requirements.txt` file in the local project 
directory into the container's `/app` directory.

```
COPY ./entrypoint.sh /app/entrypoint.sh
```

You'll want to create a `entrypoint.sh` helper script that will be run from
within the Docker container. It will take care of installing your dependencies,
migrating the book ratings table into your container's Postgres database, and
starting your Flask application. By convention, the helper script should be
named [entrypoint.sh]. Have the first line of the file be `#!/usr/bin/env bash`
to indicate that you are writing a bash script. Then, add the following `pip3`
command to install all packages listed in the copied `/app/requirements.txt`
file.

```sh
#!/usr/bin/env bash
pip3 install -r /app/requirements.txt
```

You'll need to make this entrypoint script executable. On your command line,
run:
```bash
chmod +x entrypoint.sh
```

You'll want to include this `RUN` command in the Dockerfile as well to set 
permissions and allow the copied `entrypoint.sh` script file to be 
run from within the container:

```
RUN chmod +x /app/entrypoint.sh
```

You can also add the `db upgrade` command to handle your database migrations.
But first, you'll want to be able to do so by prefacing the command with
`python3` and your entry `book_ratings.py` file, instead of `pipenv run flask`.
This way, you won't need to set the `PATH` variable that allows you to run
`flask` in a command.

As of now, your `book_ratings.py` file is simply importing the `app` from the
`/app` directory. You'll want to update the file to import `FlaskGroup` to
configure the Flask command line interface. Create a new `FlaskGroup` instance
to extend the commands connected to the Flask `app`. Python assigns the
`__name__` dunder to the string `"__main__"` whenever a script is executed.
You'll run the `book_ratings.py` lika script file, therefore assigning the
`__name__` dunder to be `"__main__"`. When the file is run as a Python script,
you'll want to initialize a CLI connection.

```python
from flask.cli import FlaskGroup
from app import app

cli = FlaskGroup(app)

if __name__ == "__main__":
    cli()
```

Add the updated `python3` commands to migrate your database and start your
application. Notice how your application is started by running the
`book_ratings.py` file as a Python script file, instead of using the `pipenv run
flask run` Flask command. You'll use `run -h 0.0.0.0` to assign the host of the
application.

```sh
#!/usr/bin/env bash
pip3 install -r /app/requirements.txt
python3 book_ratings.py db upgrade
python3 book_ratings.py run -h 0.0.0.0
```

### Create the Docker-Compose file

Now that you've finished setting up your microservice's package installation,
application setup, and Dockerfile to generate a custom Python image, it's time
to create the `docker-compose.yml` file! Begin by modeling the file based on the
compose file you created for the Express application.

**docker-compose.yml**

```yml
version: "3.8"
services:
  app:
    build: .
    image: nodeapp
    ports:
      - "80:8080"
    environment:
      DB_USERNAME: reading_list_app
      DB_PASSWORD: password
      DB_DATABASE: reading_list
      DB_HOST: postgres
      NODE_ENV: development
    networks:
      pgnodeapp:
    volumes:
      - ".:/app"
    depends_on:
      - "db"
    command: ["./wait-for", "postgres:5432", "--", "npm", "run", "build-start"]

  db:
    image: postgres:12-alpine
    environment:
      POSTGRES_USER: reading_list_app
      POSTGRES_PASSWORD: password
      POSTGRES_DB: reading_list
    volumes:
      - postgres-db:/var/lib/postgresql/data
    networks:
      pgnodeapp:
        aliases:
          - "postgres"

volumes:
  postgres-db:

networks:
  pgnodeapp:
    driver: bridge
```

Let's begin by updating the network name. Rename the `pgnodeapp` network, since
you are no longer creating a network for a Node application.

Next, update the `app` service to be an `api` service based on the custom Python
image you just created with the Dockerfile. In the `api` service, name the
custom image to be `flaskapp` instead, and publish port `5000` while listening
on port `5000`. Update the `environment` variables to the variables expected by
your Flask application.

Since you are Dockerizing the Flask microservice for local development, you can
keep the volume that bind mounts the application files. This way, whenever a
file changes locally, a running application in a container will reflect those
changes. You'll also want the `api` service to depend on the `db` service. Since
you added your package installation, database migration, and application start
commands into the `entrypoint.sh` script file, run the file in the `api`
service's `command` so that those shell commands are run within the container.

For your `db` service, all you'll need to do is update the `environment`
variables expected to set up the PostgreSQL database. Use the values from your
Flask application's database URI.

Take a moment to build your custom image and start your container by running
`docker-compose up --build`. Then, visit http://0.0.0.0:5000/ in the browser to
send a GET request to the dockerized API service. You should receive a `403
Forbidden` response because of the `@app.before_request` decorator where
requests from the local host are whitelisted. The `request.remote_addr` from
your browser's host does not match the local host within the container. For now,
comment out the whitelist function and refresh your browser. Now you should see
your test route response!

Take a moment to use Postman and test your dockerized service by sending GET and
POST request for book ratings. After you've thoroughly tested the dockerized
Flask app, comment in the `@app.before_request` whitelist function and move
forward to the next phase to implement the microservice!

## Phase 3: Implement the microservice

It's time to implement the microservice you created with Flask into your Express
app! Create a book show page that renders a book's details and ratings, using
the microservice. Then, implement a form that sends a POST request to the
microservice to allow a user to create a book rating.

Think about how you might reference your Flask microservice endpoints, before
the microservice is deployed and from within your Dockerized development
environment. You'll want to connect the containerized Express application to a
service on the host. Take a look at the [networking features in Docker]. Think
of how you might use the special DNS name, `host.docker.internal`, to send a
request from your Express application to your Flask microservice.

You'll also want to take a look at the `@app.before_request` decorator where
requests from the local host are whitelisted. Since the request will come from
within a containerized application, the `request.remote_addr` may not be the
local `127.0.0.1` IP address. You actually want to whitelist all requests from
within your containerized Express application. Think of how else you can
whitelist specific requests. Take a look at the [flask.request documentation].
Browse the request object's properties and think of how you can check whether
the special DNS name, `host.docker.internal`, is associated to an incoming
request.


[networking features in Docker]: https://docs.docker.com/docker-for-mac/networking/#use-cases-and-workarounds
[entrypoint.sh]: https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#entrypoint
[flask.request documentation]: https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data