import os
from flask import Flask, redirect, request
from flask_cors import CORS
from flask_migrate import Migrate
from flask_wtf.csrf import generate_csrf
from backend.aws_helpers import get_unique_filename, upload_file_to_s3
from backend.forms import ImageForm
from backend.config import Configuration
from backend.models import Actor, Image, db
from backend.seeds import seed_commands

app = Flask(__name__, static_folder="../frontend/dist", static_url_path="/")
app.cli.add_command(seed_commands)
app.config.from_object(Configuration)
db.init_app(app)
Migrate(app, db)
CORS(app)

@app.route("/api/actors/<string:actor_name>")
def get_actor(actor_name):
    actor = Actor.query.filter(Actor.name == actor_name).first()
    if actor is None:
        return {"message": "no actor"}, 400
    return {
        "actor": actor.to_dict(),
        "movies": [movie.to_dict() for movie in actor.movies],
    }
@app.route("/api/hello")
def hello():
    return {"hello": "world"}, 418

@app.route("/api/images")
def all_images():
    images = Image.query.all()[::-1]
    return {"images": [image.to_dict() for image in images]}

@app.route("/api/images", methods=["POST"])
def upload_image():
    print("Did i make it to the route handler?")

    form = ImageForm()

    form["csrf_token"].data = request.cookies["csrf_token"]
    print("REQUEST: ", request.form)
    print(form)

    if form.validate_on_submit():
        image = form.data["image"]
        print("IMAGE File: ", image)

        image.filename = get_unique_filename(image.filename)
        upload = upload_file_to_s3(image)
        if "url" not in upload:
            return {"message": "oops, something went wrong"}, 400
        url = upload["url"]
        new_image = Image(image=url)
        db.session.add(new_image)
        db.session.commit()
        return {"image": new_image.to_dict()}, 201

    return {"errors": form.errors}

@app.route("/api/images/<int:image_id>")
def get_image(image_id):
    image = Image.query.get_or_404(image_id)
    if image is None:
        return {"message": "no image"}, 400
    return {"image": image.to_dict()}

@app.before_request
def https_redirect():
    if os.environ.get('FLASK_ENV') == 'production':
        if request.headers.get('X-Forwarded-Proto') == 'http':
            url = request.url.replace('http://', 'https://', 1)
            code = 301
            return redirect(url, code=code)

@app.after_request
def inject_csrf_token(response):
    response.set_cookie(
        "csrf_token",
        generate_csrf(),
        secure=True if os.environ.get("FLASK_ENV") == "production" else False,
        samesite="Strict" if os.environ.get("FLASK_ENV") == "production" else None,
        httponly=True,
    )
    return response


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def react_root(path):
    """
    This route will direct to the public directory in our
    react builds in the production environment for favicon
    or index.html requests
    """
    if path == "favicon.ico":
        return app.send_from_directory("public", "favicon.ico")
    return app.send_static_file("index.html")


@app.errorhandler(404)
def not_found(e):
    return app.send_static_file("index.html")
