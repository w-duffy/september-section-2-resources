# Dockerize an Express and Postgres Application

For this phase, you'll create a `docker-compose.yml` file for a simple Express
and Postgres app. Navigate to the __team_alpha__ folder in the skeleton.
Notice how you have a full Express application as well as a `db` directory with
model, migration, and seed files. You can Dockerize this container in at least
two ways:

1. Local development: mount a volume in the container. You would bind mount a
   host path to the application by setting a `volumes` key with a value of
   `.:/app` in the `docker-compose.yml` file. This maps a local directory to the
   container so all the source code (including node_modules) stays on the local
   file system. As a reminder, you can use the `volumes` option to both
   configure a "bind mount" and a "volume". The term "volume" has a very
   specific meaning in Docker so you should only use it when referring to a
   named volume.
2. Non-local development: copy application files into custom image. You would
   use `COPY . /app` in the Dockerfile. Every time you change the source code
   for the application, you’d need to rebuild the containers.

## Phase 1: Dockerize an Express/Postgres app for local development

Today, you'll create a `docker-compose.yml` file with local development in mind.
You'll configure a bind mount in the container so all the source code stays on
the local file system. For this app, you’ll create two services: one service
named `app` for the Express application, and one service named `db` for the
PostgreSQL database.

You've already been provided with the `Dockerfile` for the custom node image
you'll be creating. Take a moment to check out the file and notice how it simply
sets the working directory and exposes the `8080` port.

### Compose file

For this Compose file, set your version to '3.8'. Create two services: `app`,
for your Express application, and `db`, for your Postgres database. Start by
filling out the Postgres `db` service.

Set your image for the `db` service to be `postgres:12-alpine`. You'll need to
set the `environment` variables expected by the image to create the database
user and database. Take a look at the [official Postgres image documentation] on
Docker Hub to determine how to set up the Postgres image. Scroll down to the
_How to extend this image_ section and take a look at the environment variables
expected in configuration:

> `POSTGRES_PASSWORD` This environment variable is required for you to use the
> PostgreSQL image. It must not be empty or undefined. This environment variable
> sets the superuser password for PostgreSQL. The default superuser is defined
> by the POSTGRES_USER environment variable.

> `POSTGRES_USER` This optional environment variable is used in conjunction with
> `POSTGRES_PASSWORD` to set a user and its password. This variable will create
> the specified user with superuser power and a database with the same name. If
> it is not specified, then the default user of postgres will be used.

> `POSTGRES_DB` This optional environment variable can be used to define a
> different name for the default database that is created when the image is
> first started. If it is not specified, then the value of POSTGRES_USER will be
> used.

Notice how the documentation states which environment variables are required and
which are optional. Since you configured the application by creating a database
user with a password and a database connected to that user, you'll need to set
the `POSTGRES_USER`, `POSTGRES_PASSWORD`, and `POSTGRES_DB` so that your
Postgres image will create a user and database in a similar fashion.

Use the `DB_USERNAME`, `DB_PASSWORD`, `DB_DATABASE` values set in the
`.env.example` file.

```
PORT=8080
DB_USERNAME=reading_list_app
DB_PASSWORD=password
DB_DATABASE=reading_list
DB_HOST=postgres
```

You'll also want to set up a volume for the database so your data persists
between using the `docker compose up` command multiple times. Name your volume
`postgres-db` and have it point to where the Postgres image keeps its volumes
`/var/lib/postgresql/data`. Remember that if you have a named volume, you have
to name it outside the `service` key and under a `volumes` key. Take a look at
the [Docker Compose 3] documentation for volumes if you need syntax reference.

Next, you'll want to create a custom network you can reference by name to
connect your database and Node app. Just like how your `volumes` key it outside
of your `services`, you create a new key for `networks`. Name your custom
network "pgnodeapp" and use the default `bridge` driver. It'll look something
like this:

```yaml
networks:
  pgnodeapp:
    driver: bridge
```

Now you'll want your `db` service to connect to your custom network by adding a
`networks` key referencing the named "pgnodeapp" network. You can also alias it
as "postgres". Your `db` service should contain a `networks` key, like so:

```yaml
# CODE SHORTENED FOR BREVITY
   db:
      # CODE SHORTENED FOR BREVITY
      networks:
         pgnodeapp:
         aliases:
            - "postgres"
```

Now let's start building the `app` service. If you need a reminder on building
images with Compose, check out the [Docker documentation][build-docs] on the
subject. In your `app` service, build a new image based on the `Dockerfile` you
have been provided. You can do this by using a `build` key under your `app`
service. The `build` key takes a path to the build context (i.e. where Compose
can find the Dockerfile to use for the build). Instruct the service to build the
current path by using `.`. Your current `app` service should look something like
this:

```yaml
services:
  app:
    build: .
```

You can use the `image` key to name the new image as `nodeapp`. Now have your
Express application run on port 8080 by publishing your local port `80` and
using port `8080` in the container. Feel free to reference the [ports section]
of the Docker documentation.

Now you'll connect the `app` and `db` services. Your `app` service will need to
be passed environment variables it expects to configure the database connection.
Check out the `.env.example` file and configure your service to set the expected
environment variables: `DB_USERNAME`, `DB_PASSWORD`, `DB_DATABASE`, `DB_HOST`,
and `NODE_ENV`.

Lastly, you'll want mount the local directory for your `nodeapp` image to
reference. This mounts _all_ (`.`) of the local directory to the image's `/app`
directory.

```yaml
app:
   # CODE SHORTENED FOR BREVITY
   volumes:
      - ".:/app"
```

Now let's connect your services together! Connect the `app` container to the
`pgnodeapp` network. Think of the syntax for how you connected your `db` service
to the `pgnodeapp` network. Note that you do not need to have an alias for this
connection.

### Control service startup

In order for your migration and seed commands to run after your database service
is fully up and running, you'll need to control the order of service startup by
using the `depends_on` option and an open source project, `wait-for`. This is a
common issue with a best-practice approach to [control startup and shutdown
order in Compose], as documented in the official Docker docs. Take a moment to
read about the common problem.

Let's follow this best practice approach by adding a `depends_on` key to the
`app` service. Have the `app` service depend on the `db` service.

Next, you'll have your `app` service run the `npm run build-start` command after
waiting for the Postgres database to be set up. Take a moment to check out the
`build-start` script viewing the project's `package.json` file. Notice how the
`built-start` script runs `npm install` as well as the custom `migrate` and
`seed` scripts that take care of running Sequelize commands to set up your
database. 

In order to have your container run the `npm run build-start` command after the
Postgres database is set up, you'll need the container to run a [wait-for]
script beforehand. Notice how you have a `wait-for` file in the root of the
project directory. This [wait-for] file is an open-source project to synchronize
services.

Note the example command listed in the project repository's [README][wait-for]:
`command: sh -c './wait-for db:5432 -- npm start'`.

Also note the example command listed in the [Docker docs][control startup and
shutdown order in Compose]: `command: ["./wait-for-it.sh", "db:5432", "--",
"python", "app.py"]`.

Use these two examples to build your `command` that:

1. Runs the `./wait-for` script
2. Connects the `postgres` database to local host (`5432`)
3. Runs the `npm run build-start` command

After you have set up your `app` service's `command`, be sure to set the execute
permissions for the `wait-for` script by running `chmod +x wait-for`. Then,
start your containers in with `docker-compose up` and view your running
containers in another tab with `docker-compose ps`.

> **Reminder:** you'll need to use the `docker-compose up --build` command with
> the `--build` flag whenever you make changes to any Dockerfiles or the
> `docker-compose.yml` file.

```ssh
    Name                  Command               State          Ports        
----------------------------------------------------------------------------
phase2_app_1   docker-entrypoint.sh ./wai ...   Up      0.0.0.0:80->8080/tcp
phase2_db_1    docker-entrypoint.sh postgres    Up      5432/tcp
```

Head to `http://0.0.0.0:80` and you should see your _Reading List_ application
running. Browse around and create a couple of books! You should be able to
refresh and your books should stay right where they are, even if you empty the
browser cache and do a hard reload.

To test that your named volume was installed properly, use `docker-compose down`
and then use `docker-compose up` again. The books you created should still
exist, and your application should be rendering duplicate books because the same
Postgres database was seeded again when the `npm run build-start` command ran
again in the second `docker-compose up`. 

> **Reminder:** you'll need to use the `docker-compose up --build` command with
> the `--build` flag whenever you make changes to any Dockerfiles or the
> `docker-compose.yml` file.

Amazing job! What you just accomplished in this phase is considered to be
relatively advanced Docker stuff. Now you are ready to use your Docker container
for local development!


[build-docs]: https://docs.docker.com/compose/compose-file/#build
[official Postgres image documentation]: https://hub.docker.com/_/postgres
[Docker Compose 3]: https://docs.docker.com/compose/compose-file/#volumes 
[ports section]: https://docs.docker.com/compose/compose-file/#ports 
[control startup and shutdown order in Compose]: https://docs.docker.com/compose/startup-order/
[wait-for]: https://github.com/eficode/wait-for
