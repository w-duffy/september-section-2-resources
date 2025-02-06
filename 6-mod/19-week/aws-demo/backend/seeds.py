from flask.cli import AppGroup
from backend.models import db, Actor, Movie, Image
from sqlalchemy.sql import text

seed_commands = AppGroup("seed")


@seed_commands.command("all")
def seed():
    print("RUNNING SEEDERS")

    tom_hanks = Actor(name="Tom", age=60, bio="cool!")
    ben_af = Actor(name="Ben", age=40, bio="nice!")
    renne_z = Actor(name="Renne", age=30, bio="Awesome!")

    db.session.add(tom_hanks)
    db.session.add(ben_af)
    db.session.add(renne_z)

    forest_gump = Movie(title="Forest Gump", year=2003)
    batman = Movie(title="Batman", year=2001)
    toy_story = Movie(title="toy_story", year=1993)

    tom_hanks.movies.append(toy_story)

    forest_gump.actors.append(tom_hanks)
    forest_gump.actors.append(ben_af)
    forest_gump.actors.append(renne_z)

    taco_party = Image(image ="https://helloworldfroms3.notarealobject.jpg")

    db.session.add(taco_party)
    db.session.add(forest_gump)
    db.session.add(batman)
    db.session.add(toy_story)
    db.session.commit()


@seed_commands.command("undo")
def undo():
    print("Undoing SEEDERS")
    db.session.execute(text("DELETE FROM actors"))
    db.session.execute(text("DELETE FROM movies"))
    db.session.execute(text("DELETE FROM movie_actors"))
    db.session.execute(text("DELETE FROM images"))
    db.session.commit()
