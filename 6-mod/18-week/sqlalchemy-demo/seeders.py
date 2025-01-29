from dotenv import load_dotenv
from datetime import datetime, timedelta
from random import randint

load_dotenv()
from app import app
from app.models import db, likes, Post, User, Comment

def random_date_2023():
    """Generate a random created_attime between start and end which
    should be created_attime objects"""
    start = datetime(2023, 1, 1)
    end = datetime.now()
    random_created_at = start + timedelta(
        seconds=randint(0, int((end - start).total_seconds())),
    )
    return random_created_at



with app.app_context():
    db.drop_all()
    print("Dropped all tables")
    db.create_all()
    print("Created all tables~!")

    bobbo = User(name="Bobbo", bio="Bobbo's bio is sweet!")
    # stevo = User(name="Stevo", bio="Bobbo's bio is sweet!")
    db.session.add(bobbo)
    db.session.commit()
    # print("\n\n\n\nBOBBO\n\n\n\n", bobbo.to_dict()["id"], "\n\n\n\n\n\n")
    # print(bobbo)
    bobbos_post = Post(author_id=bobbo.to_dict()["id"], caption="BOBBO Sweet post!")
    bobbos_post2 = Post(author_id=bobbo.to_dict()["id"], caption="BOBBO Sweet post TWO!")
    db.session.add(bobbos_post)
    db.session.add(bobbos_post2)
    db.session.commit()

    print("\n\n\n\nBOBBO\n\n\n\n", bobbo.posts, "\n", bobbo.liked_posts,  "\n\n\n\n\n\n")

    bobbo.liked_posts.append(bobbos_post)
    bobbo.liked_posts.pop()

    print("\n\n\n\nBOBBO\n\n\n\n", bobbo.posts, "\n", bobbo.liked_posts,  "\n\n\n\n\n\n")
    # print("\n\n\n\nBOBBO\n\n\n\n", bobbos_post.author, "\n\n\n\n\n\n")

    # db.session.add(stevo)



    will_posts = [
        {
            "caption": "hello!",
            "image": "https://pipstagram.s3.amazonaws.com/137336008_406744080656046_3364448327964401597_n.jpg",
            "created_at": random_date_2023(),
        },
        {
            "caption": "you would've gotten that stick... if you knew how to swim",
            "image": "https://pipstagram.s3.amazonaws.com/14736358_1218308304908741_9131677530216988672_n.jpg",
            "created_at": random_date_2023(),
        },
        {
            "caption": "please, just give me another hour",
            "image": "https://pipstagram.s3.amazonaws.com/147984230_349580496062106_6664809776347526236_n.jpg",
            "created_at": random_date_2023(),
        },
        {
            "caption": "my best buddy!",
            "image": "https://pipstagram.s3.amazonaws.com/15035574_1079682388796264_6184137089534132224_n.jpg",
            "created_at": random_date_2023(),
        },
        {
            "caption": "Ready for the job interview",
            "image": "https://pipstagram.s3.amazonaws.com/17332517_1437522652946724_7128079981032243200_n.jpg",
            "created_at": random_date_2023(),
        },
        {
            "caption": "let's just be friends",
            "image": "https://pipstagram.s3.amazonaws.com/18012097_255074681625671_5096963914957062144_n.jpg",
            "created_at": random_date_2023(),
        },
    ]
    zaviar_posts = [   {
            "caption": "allow me to introduce myself",
            "image": "https://pipstagram.s3.amazonaws.com/2023-07-17+14.53.08.jpg",
            "created_at": random_date_2023(),
        },

    ]
    sams_posts =[    {
            "caption": "mmmm... dirt!",
            "image": "https://pipstagram.s3.amazonaws.com/2023-07-17+14.53.30.jpg",
            "created_at": random_date_2023(),
        },
        {
            "caption": "please sir, i beg of you",
            "image": "https://pipstagram.s3.amazonaws.com/2023-07-17+14.57.09.jpg",
            "created_at": random_date_2023(),
        }
    ]

    users = [
        {
            "name": "Will",
            "bio": "Nice bio will"
        },
        {
            "name": "Zaviar"
        },
        {
            "name": "Sam"
        },
        {
            "name": "Alexi"
        }
    ]

    for user in users:
        current_user = User(**user)
        db.session.add(current_user)




    for post in will_posts:
        current_post = Post(**post)
        user_1 = User.query.get(2)
        # current_post.author_id = 1
        # current_post.user = user_1
        user_1.posts.append(current_post)
        db.session.add(current_post)

    for post in zaviar_posts:
        current_post = Post(**post)
        user_2 = User.query.get(3)
        current_post.author = user_2
        db.session.add(current_post)

    for post in sams_posts:
        current_post = Post(**post)
        user_3 = User.query.get(4)
        current_post.author = user_3
        db.session.add(current_post)

    comment = Comment(body="Buzzer beater!", user_id=2, post_id=1)
    db.session.add(comment)
    db.session.commit()
