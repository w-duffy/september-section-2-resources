# Postgres info


In the backend/package.json, you will see some scripts to help manage postgres


1. create a user

```sh
psql -c "CREATE USER <user> WITH PASSWORD 'password' CREATEDB"
```

2. create a database

```sh
psql -c "CREATE DATABASE <databasename>"
```

3. fill in the information in the .env based on the .env example using the same info you used in steps 1 and 2



Make sure to install postgres, psql, and postbird.

1. you will want to connect psql to your computers user account so that it can connect to postbird
2. You will want to use postbird to view the database (although you can also use psql cli to view it in terminal)



Postbird install: https://github.com/Paxa/postbird
Postgres install: https://www.postgresql.org/download/
