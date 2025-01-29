from flask import Flask
from app.config import Config
from .models import db, User, Post
from sqlalchemy.orm import joinedload


app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

# {"Spots": [{Reviews: [], SpotImages: []}]}

@app.route("/new")
def new():
    # users = db.session.execute(db.select(User)).scalars()
    bobbo = User.query.filter(User.name == "Bobbo").first()
    # bobbo = Post.query.filter(Post.name == "Bobbo").first()
    print(bobbo)
    print("GET ALL", bobbo)
    return {"UserDetails": bobbo.to_dict_with_posts()}




# READ all
@app.route("/")
def index():
    # users = db.session.execute(db.select(User)).scalars()
    users = User.query.all()
    # print("GET ALL", users)
    return [user.to_dict() for user in users]




# READ one
@app.route("/<int:id>")
def get_user(id):
    user = User.query.get(id)
    return user.to_dict_with_posts()


# CREATE new
@app.route("/new")
def create_user():
    # Object takes in kwargs
    new_user = User(name="Stevo")
    print(new_user)
    db.session.add(new_user)
    db.session.commit()
    return new_user.to_dict()

\
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

@app.route("/likes")
def create_likes():
    will = User.query.filter(User.name == "Will").first()
    print(will.liked_posts)
    will.posts
    print(will.to_dict())
    wills_posts = Post.query.filter(Post.author_id == 2).first()
    print(wills_posts)
    will.liked_posts.append(wills_posts)
    db.session.commit()
    return "Success!"

# Lazy vs Eager loading
@app.route("/loading")
def testing():

    # users = User.query.all()
    # # https://docs.sqlalchemy.org/en/14/orm/loading_relationships.html#sqlalchemy.orm.joinedload
    users = User.query.options(joinedload(User.posts)).all() # eager loading

    print("\n ~~~~~~~~~~~~~~ \n")
    return [user.to_dict_with_posts() for user in users]
