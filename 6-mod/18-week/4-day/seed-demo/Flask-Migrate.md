# Alembic + Flask = Flask-Migrate

## Sqlite3 DB URL Reminder

Remember that this URL is different than how it was set in Express!

```python
DATABASE_URL=sqlite:///db_name.db
```

## Using Alembic by itself

If you wanted to use Alembic without Flask, here's how you'd do it!

Of course, start by installing it

```zsh
pipenv install alembic
```

### Remember `npx sequelize init`?

Well Alembic has it's own version!

This creates a folder structure for Alembic to operate within

```zsh
pipenv run alembic init migrations
```

The `migrations` is the folder name - can be anything you want!

Let's take a look at the stuff we just created

### `versions` directory

Your migrations (aka revisions) will go in here!

### `script.py.mako`

Remember how Sequelize would give you boilerplate code every time you created a migration?

```js
'use strict';

module.exports = {
  up: async (queryInterface, Sequelize) => {
    /**
     * Add altering commands here.
     *
     * Example:
     * await queryInterface.createTable('users', { id: Sequelize.INTEGER });
     */
  },

  down: async (queryInterface, Sequelize) => {
    /**
     * Add reverting commands here.
     *
     * Example:
     * await queryInterface.dropTable('users');
     */
  },
};
```

Well Alembic lets us decide what that boilerplate looks like!

By default, it should have everything you need, but if you wanted to modify it, you can!

### `env.py`

Think of this like your `.env` and `.flaskenv` files, except it's specifically for Alembic

### `alembic.ini`

This file has TONS of options in it for us to customize how Alembic works

You can deep dive on this if you'd like, but something everyone can do is comment in this line:

```py
# file_template = %%(year)d_%%(month).2d_%%(day).2d_%%(hour).2d%%(minute).2d-%%(rev)s_%%(slug)s
```

This simply gives us a timestamp on our migration files, making it easier to keep track of the order that things ran in

### Revisions === Migrations

Make a revision

```zsh
pipenv run alembic revision -m "the message about the revision"
```

`op` = alembic

`sa` = SQLAlchemy

Run this to apply revisions to your db

```zsh
pipenv run alembic upgrade head
```

Run this to see the history of revisions

```zsh
pipenv run alembic history
```

## Flask-Migrate

Just install `flask-migrate`!

```zsh
pipenv install flask-migrate
```


That'll give us `alembic` too!

### Setup ain't too different

Our `project-name/app/__init__.py` simply needs to add `Migrate`

```py
from flask import Flask
from flask_migrate import Migrate

from .config import Config
from .models import db

app = Flask(__name__)

app.config.from_object(Config)
db.init_app(app)
Migrate(app, db)
```

### Initialize Alembic

```zsh
pipenv run flask db init
```

Same files from before when setting up without Flask

## Add a model

This is just normal model creating syntax

```py
# /project-name/app/models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Owner(db.Model):
    __tablename__ = "owners"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(255), nullable=False)
```

### Autogenerate a migration

```zsh
pipenv run flask db migrate -m "create owners table"
```

### Note from the [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/) docs:

> The migration script needs to be reviewed and edited, as Alembic is not always able to detect every change you make to your models. **_`In particular, Alembic is currently unable to detect table name changes, column name changes, or anonymously named constraints.`_** A detailed summary of limitations can be found in the [Alembic autogenerate](https://alembic.sqlalchemy.org/en/latest/autogenerate.html#what-does-autogenerate-detect-and-what-does-it-not-detect) documentation.

### Apply it to the database

```zsh
pipenv run flask db upgrade
```

### Undo a migration

```zsh
pipenv run flask db downgrade
```
