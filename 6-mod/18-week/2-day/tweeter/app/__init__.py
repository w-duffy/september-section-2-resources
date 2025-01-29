from datetime import date
from random import choice

from flask import Flask, redirect, render_template, request

from .config import Config
from .forms import NewTweetForm
from .tweets import tweets
from flask_se
app = Flask(__name__)

app.config.from_object(Config)



@app.route("/")
def index():
    random_tweet = choice(tweets)
    return render_template("base.html", path=request.path, tweet=random_tweet)


@app.route("/feed")
def feed():
    return render_template("base.html", path=request.path, tweets=tweets)


@app.route("/new", methods=["GET", "POST"])
def post_a_tweet():
    tweet_form = NewTweetForm()

    if tweet_form.validate_on_submit():
        new_tweet = {
            id: len(tweets),
            "author": tweet_form.data["author"],
            "tweet": tweet_form.data["tweet"],
            "date": date.today(),
            "likes": 0,
        }
        tweets.append(new_tweet)
        return redirect("/feed")

    if tweet_form.errors:
        return render_template(
            "base.html", path=request.path, form=tweet_form, **tweet_form.errors
        )

    return render_template("base.html", path=request.path, form=tweet_form)
