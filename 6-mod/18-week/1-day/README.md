# HW Heavy Day

Work through your HW readings, be sure to code along!

Check out the lecture notes for more condensed content review

This file will help us get started from scratch

## Flask app setup

1. Install flask in your project folder

   ```bash
   # /project-name
   pipenv install flask
   ```

2. Create a folder for your application with a `__init__.py`.

   ```bash
   # /project-name
   mkdir app

   cd app

   # /project-name/app
   touch __init__.py
   ```

3. Select your interpreter in VSCode

   Enter your virtual environment folder from the project root

   ```bash
   # /project-name
   cd .venv

   # Copy the output - this is the path to your virtual env!
   pwd # .../project-name/.venv
   ```

   Click on `Python: Select Interpreter`

   Paste the path to your project's virtual environment

4. Import `Flask` in the `__init__.py`

   ```python
   from flask import Flask
   ```

5. Instantiate a `Flask` instance

   ```python
   app = Flask(__name__)
   ```

6. Add a `.flaskenv` file. This file sets publicly visible environment variables for your Flask app

   ```bash
   # /project-name/.flaskenv
   FLASK_APP=simple.py
   FLASK_DEBUG=True
   ```

7. Install python-dotenv to load environment variables into the app configuration

   ```bash
   # /project-name
   pipenv install python-dotenv
   ```

8. Run your application!

   ```bash
   # /project-name
   pipenv run flask run
   ```

---

### Adding a secret key (or other configuration variables)

In addition to the `.flaskenv` file which contains environment specific (not secret) information, we can use a `.env`.

This file contains environment variables we want to keep secret. Unlike `.flaskenv`, it will _not_ be committed to GitHub.

This should exist in your project's root directory, just like `.flaskenv`

```bash
# /project-name/.env
SECRET_KEY=SomeSecret
```

---

### Making a Config class

Get the secret values from your `.env` and define a `Config` class which has all of the values you want to incorporate into your app.

```python
# /project-name/app/config.py
import os


class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY')
```

Then incorporate these values into your application using the the `config.from_object method`.

```python
# /project-name/app/__init__.py
from flask import Flask
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)
```
