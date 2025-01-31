from .db import db

likes = db.Table(
    "likes",
    db.Column("author_id", db.Integer, db.ForeignKey("users.id"), primary_key=True),
    db.Column("post_id", db.Integer, db.ForeignKey("posts.id"), primary_key=True),
)



class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    posts = db.relationship("Post", back_populates="author")
    # posts = db.relationship("Post", back_populates="author", lazy="joined") # Eager loads the user's posts anytime you query for users; better to eagerly load on a per route basis
    liked_posts = db.relationship(
        "Post", secondary="likes", back_populates="user_likes"
    )


    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
        }

    def to_dict_with_posts(self):
        return {
            "id": self.id,
            "name": self.name,
            "Posts": [post.to_dict() for post in self.posts],
        }
