from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
from .models import db, User, Post
from sqlalchemy.orm import joinedload
from flask_migrate import Migrate
from .seeders import seed_command

app = Flask(__name__)

app.cli.add_command(seed_command)

app.config.from_object(Config)

db.init_app(app)
Migrate(app, db)


# READ all
@app.route("/")
def index():
    # users =
    users = User.query.all()
    print("GET ALL", users)

    return [user.to_dict() for user in users]



# READ one
@app.route("/<int:id>")
def get_user(id):
    user = User.query.get(id)
    post = Post.query.get(7)
    user.liked_posts.append(post)
    db.session.commit()
    return user.to_dict_with_posts()





# CREATE new
@app.route("/new")
def create_user():
    # Object takes in kwargs
    new_user = User(name="Will")
    print(new_user)
    db.session.add(new_user)
    db.session.commit()
    return new_user.to_dict()


# Update
@app.route("/update/<int:id>")
def update_user(id):
    user = User.query.get(id)
    user.name = "new name"
    print(user)
    db.session.commit()
    return user.to_dict()



# Delete
@app.route("/delete/<int:id>")
def delete_user(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return "Success!"



# Eager vs Lazy 
@app.route("/loading")
def testing():
    users = User.query.all()
    # # https://docs.sqlalchemy.org/en/14/orm/loading_relationships.html#sqlalchemy.orm.joinedload
    # users = User.query.options(joinedload(User.posts)).all()
    print("\n ~~~~~~~~~~~~~~ \n")
    return [user.to_dict_with_posts() for user in users]
