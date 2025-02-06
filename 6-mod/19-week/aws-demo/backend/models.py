from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

movie_actors = db.Table(
    "movie_actors",
    db.Column("actor_id", db.Integer, db.ForeignKey("actors.id"), primary_key=True),
    db.Column("movie_id", db.Integer, db.ForeignKey("movies.id"), primary_key=True),
)

class Actor(db.Model):
    __tablename__ = "actors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer)
    bio = db.Column(db.String(2000))

    movies = db.relationship("Movie", secondary=movie_actors, back_populates="actors")

    def to_dict(self):
        return {"id": self.id, "name": self.name}


class Movie(db.Model):
    __tablename__ = "movies"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer)

    actors = db.relationship("Actor", secondary=movie_actors, back_populates="movies")

    def to_dict(self):
        return {"id": self.id, "title": self.title, "year": self.year}


class Image(db.Model):
    __tablename__ = "images"

    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(500), nullable=False) # this should've been called image_url
    # Don't forget a foreign key col!
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    def to_dict(self):
        return {"id": self.id, "image": self.image}
