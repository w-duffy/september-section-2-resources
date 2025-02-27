from datetime import datetime
from .db import db

class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    caption = db.Column(db.String(2000))
    image = db.Column(db.String(1000), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    author = db.relationship("User", back_populates="posts")
    user_likes = db.relationship("User", secondary="likes", back_populates="liked_posts")

    def to_dict(self):
        return {
            "caption": self.caption,
            "image": self.image
        }
