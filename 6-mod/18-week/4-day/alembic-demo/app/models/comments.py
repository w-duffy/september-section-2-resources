from .db import db


class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    caption = db.Column(db.String(250), nullable=False)
    commentor = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    image = db.Column(db.String(250), nullable=False)
    post_date = db.Column(db.Date, nullable=False)
