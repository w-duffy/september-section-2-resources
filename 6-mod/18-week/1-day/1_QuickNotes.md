# Quick notes on pipenv, Sqlite3, & Flask

## Hate squigglies?

`# noqa` - stop python linter from being mad

## python, pip, pipenv vs node, npm

Run file

- node index.js
- python index.py

Install things

- npm install express
- pip install flask
  - This installs to your computer!!!
  - Not usually what we want
- pipenv install flask
  - This installs to your virtual environment
  - We will always be working within a virtual environment

## Python Sqlite3

- cursor
  - Tool to navigate through our database
- cursor.execute()
  - Runs SQL commands
    - `curs.execute('SELECT firstName FROM users;')`

## Running a flask app

`pipenv run flask run`

- Should be in your backend's root directory

`pipenv run flask run -p 5001`

- To set a specific port to run on

`pipenv shell`

- Directly enter the environment
  - Don't have to run `pipenv run` in front of other commands now

## .flaskenv

Flask uses `.flaskenv` in addition to `.env`

- `.env` should NEVER be public-facing
- `.flaskenv` is necessary to be public-facing
  - We're running in a special python environment
  - Any non-private things that env needs to run should be here

To use `.env` in Node apps

```shell
npm install dotenv
```

To use `.flaskenv` and `.env` in Flask apps

```shell
pipenv install python-dotenv
```

Then create a `.flaskenv` and fill it with your environment variables

### `FLASK_APP=name_of_file(.py)`

- If you want flask to run a single file, put file name
- If you want flask to run a module (entire folder's contents), put folder name
  - The folder you're running must have a `__init__.py` file
  - This file collects and runs everything else in your folder

### `FLASK_ENV=development`

- Same situation as express
- Additionally, add `FLASK_DEBUG=true` to remove deprecated console warning

### `SECRET_KEY=preferablyRandomlyGenerated`

- Same situation as express

## Using `config`

Config is just an object

Can create key-value pairs on app.config directly

Better to create a Config class, add all variables there, then add our Config class to app.config

`.from_object(Your_Config_Here)` adds your config to app.config
