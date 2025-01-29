# Flask-SQLAlchemy Setup Guide

Here's how you should be setting up an app with Flask, WTForms, and SQLAlchemy

## 1. Do your normal project setup

- I usually start by creating:

  - Project folder

  - `app` folder

  - `__init__.py` file inside of `app`

## 2. Install dependencies

```zsh
 pipenv install flask flask-wtf flask-sqlalchemy python-dotenv
```

## 3. Set up your environment

- Make sure VSCode is pointing to the right `.venv`

- Create a `.flaskenv`

```env
FLASK_APP=app
DEBUG_MODE=1
```

- Create a `.env`

```env
SECRET_KEY=generate_a_secret
DATABASE_URL=sqlite:///dev.db
```

## 4. Create our Config class

```python
# /project-name/app/config.py
import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
```

## 5. Create an instance of SQLAlchemy

```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
```

## 6. Connect it all to our app

```python
# /project-name/app/__init__.py
from flask import Flask
from .config import Config
from .models import db

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
```

## Now we're good to start making models!
