from flask import Flask, render_template, redirect
from .config import Config
# from .posts import posts
from .routes.post_routes import posts
from .routes.user_routes import users
from .models import db, User, Post
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# print(__name__)
app.config.from_object(Config)

db.init_app(app)

Migrate(app, db)





app.register_blueprint(posts, url_prefix="/posts")
app.register_blueprint(users, url_prefix="/users")



@app.route("/")
def index():
    """home route will return the landing page"""
    # Query
    return render_template("index.html")
    # return redirect("/another")


# @app.route("/another")
# def another_route():
#     return "<h1>This is totally a different route!</h1>"



@app.route("/all")
def get_all_posts():
    """get all the posts and return them """
    # all_post = Post.query.all()
    return render_template("feed.html", posts=posts)


@app.route("/<int:id>")
def get_post_by_id(id):
    """return a single post by the id passed to the route"""
    # one_post = Post.query.get(id)
    one_post = [post for post in posts if post["id"] == id ]
    print(one_post)
    return render_template("feed.html", posts=one_post )



# @app.route("/seed-data")
# def seeder():
#     user1 = User(
#         username="Patch",
#         email="path_the_cat@gmail.com",
#         profile_pic="https://res.cloudinary.com/app-academy4/image/upload/v1647912257/Patchstagram/IMG_3074_ubqe1e.jpg",
#         bio="I love naps and food"
#     )

#     user2 = User(
#             username="Blueberry44",
#             email="blue@aol.com",
#             profile_pic="https://res.cloudinary.com/app-academy4/image/upload/v1647912128/Patchstagram/66346842095__0566A55A-DF10-4E86-A59A-F5694436FA4E_wmoi1w.jpg",
#             bio="I am a ninja! 🥷🏻",
#     )

#     user3 = User(
#             username="brads213",
#             email="brad@gmail.com",
#             profile_pic="https://ca.slack-edge.com/T03GU501J-USQFVK3GT-941e867a316f-512",
#             bio="I am the father of 2 crazy cats",
#     )

#     all_users = [user1, user2, user3]
#     _ = [db.session.add(user) for user in all_users]
#     db.session.commit()
#     print("Users created!")

#     post1 = Post(
#         caption="Napping outside is always fun...",
#         image="https://res.cloudinary.com/app-academy4/image/upload/v1647912033/Patchstagram/IMG_3394_fktg48.jpg",
#         post_date=fake.date_between(start_date="-1y", end_date="today"),
#         user=choice(all_users),
#         post_likes=[user2, user3]
#     )

#     post2 = Post(
#         caption="Napping inside is pretty awesome too...",
#         image="https://res.cloudinary.com/app-academy4/image/upload/v1647912403/Patchstagram/64865942444__2B7B1A74-ECAF-4798-BEAB-D4890B7164C4_hnmowy.jpg",
#         post_date=fake.date_between(start_date='-1y', end_date='today'),
#         user=choice(all_users),
#         post_likes=[user2, user1],
#     )

#     post3 = Post(
#         caption= "I like my fish",
#         image= "https://res.cloudinary.com/app-academy4/image/upload/v1647912006/Patchstagram/IMG_3437_u2frrk.jpg",
#         post_date=fake.date_between(start_date='-1y', end_date='today'),
#         user=choice(all_users),
#         post_likes=[user1, user2, user3],
#     )

#     post4 = Post(
#         caption= "Now THIS is a party!",
#         image= "https://res.cloudinary.com/app-academy4/image/upload/v1647912056/Patchstagram/IMG_3389_i6czzx.jpg",
#         post_date=fake.date_between(start_date='-1y', end_date='today'),
#         user=choice(all_users),
#     )

#     post5 = Post(
#         caption= "This punk stole my tent! ⛺️",
#         image= "https://res.cloudinary.com/app-academy4/image/upload/v1647912094/Patchstagram/IMG_3211_sy5wcy.jpg",
#         post_date=fake.date_between(start_date='-1y', end_date='today'),
#         user=user2,
#         post_likes=[user2, user3]
#     )

#     all_posts = [post1, post2, post3, post4, post5]
#     _ = [db.session.add(post) for post in all_posts]
#     db.session.commit()
#     print('POSTS SEEDED TO DB')
