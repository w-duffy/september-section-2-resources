import os
import uuid
from datetime import datetime
from flask import Flask, render_template, request, session, redirect
from flask_cors import CORS
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect, generate_csrf
from flask_login import LoginManager, login_required
from .models import db, User
from .api.user_routes import user_routes
from .api.auth_routes import auth_routes
from .seeds import seed_commands
from .config import Config
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
import boto3

app = Flask(__name__, static_folder='../react-vite/dist', static_url_path='/')

# Setup login manager
login = LoginManager(app)
login.login_view = 'auth.unauthorized'


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


# Tell flask about our seed commands
app.cli.add_command(seed_commands)

app.config.from_object(Config)
app.register_blueprint(user_routes, url_prefix='/api/users')
app.register_blueprint(auth_routes, url_prefix='/api/auth')
db.init_app(app)
Migrate(app, db)

# Application Security
CORS(app)

BUCKET_NAME = '2024-june-terraform-demo'
S3_LOCATION = f"https://{BUCKET_NAME}.s3.amazonaws.com/"

s3 = boto3.client(
   "s3",
   aws_access_key_id=os.environ.get("S3_KEY"),
   aws_secret_access_key=os.environ.get("S3_SECRET"),
)


def get_unique_filename(filename):
    ext = filename.rsplit(".", 1)[1].lower()
    unique_filename = uuid.uuid4().hex
    return f"{unique_filename}.{ext}"


def upload_file_to_s3(file, acl="public-read"):

    try:
        s3.upload_fileobj(
            file,
            BUCKET_NAME,
            file.filename,
            ExtraArgs={
                "ACL": acl,
                "ContentType": file.content_type
            }
        )
    except Exception as e:
        # in case the your s3 upload fails
        print("full error:", e)
        return {"errors": str(e)}

    return {"url": f"{S3_LOCATION}{file.filename}"}


def remove_file_from_s3(image_url):
    # AWS needs the image file name, not the URL,
    # so you split that out of the URL
    key = image_url.rsplit("/", 1)[1]
    try:
        s3.delete_object(
        Bucket=BUCKET_NAME,
        Key=key
        )
    except Exception as e:
        return { "errors": str(e) }
    return True

ALLOWED_EXTENSIONS = {"pdf", "png", "jpg", "jpeg", "gif", "webp"}

class ImageForm(FlaskForm):
    image = FileField("Image File", validators=[FileRequired()])
    # image = FileField("Image File", validators=[FileRequired(), FileAllowed(list(ALLOWED_EXTENSIONS))])


class Image(db.Model):
    __tablename__ = "images"

    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    def to_dict(self):
        return {"id": self.id, "image": self.image}

# Gets all images from the database
@app.route("/api/images")
def all_images():
    images = Image.query.all()
    return {"images": [image.to_dict() for image in images]}, 200

# Create a new image
@app.route("/api/images", methods=["POST"])
@login_required
def upload_image():
    form = ImageForm()
    form["csrf_token"].data = request.cookies["csrf_token"]
    print(form.data)

    if form.validate_on_submit():
        print("here")

        image = form.data["image"]
        image.filename = get_unique_filename(image.filename)
        upload = upload_file_to_s3(image)
        print(upload)

        if "url" not in upload:
            return {"error": "Woopsie daisy, plz try again. Thx!"}, 500

        url = upload["url"]
        new_image = Image(image=url)
        db.session.add(new_image)
        db.session.commit()

        return {"image": new_image.to_dict()}, 201

    return {"errors": form.errors}

# Get image by id
@app.route("/api/images/<int:image_id>")
def get_image(image_id):
    image = Image.query.get(image_id)
    if image is None:
        return {"message": "no image"}, 404
    return {"image": image.to_dict()}

# Update an image
@app.route("/api/images/<int:image_id>", methods=["PUT"])
@login_required
def update_image(image_id):
    image = Image.query.get(image_id)
    if image is None:
        return {"message": "Image not found"}, 404

    form = ImageForm()
    form["csrf_token"].data = request.cookies["csrf_token"]

    if form.validate_on_submit():
        # Delete old image from S3
        remove_file_from_s3(image.image)

        # Upload new image to S3
        new_image = form.data["image"]
        new_image.filename = get_unique_filename(new_image.filename)
        upload = upload_file_to_s3(new_image)

        if "url" not in upload:
            return {"error": "Failed to upload new image"}, 500

        # Update image URL in database
        image.image = upload["url"]
        db.session.commit()

        return {"image": image.to_dict()}, 200

    return {"errors": form.errors}, 400

# Delete an image
@app.route("/api/images/<int:image_id>", methods=["DELETE"])
@login_required
def delete_image(image_id):
    image = Image.query.get(image_id)
    if image is None:
        return {"message": "Image not found"}, 404

    # Remove from S3
    remove_file_from_s3(image.image)

    # Remove from database
    db.session.delete(image)
    db.session.commit()

    return {"message": "Successfully deleted"}, 200

# Since we are deploying with Docker and Flask,
# we won't be using a buildpack when we deploy to Heroku.
# Therefore, we need to make sure that in production any
# request made over http is redirected to https.
# Well.........
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
        'csrf_token',
        generate_csrf(),
        secure=True if os.environ.get('FLASK_ENV') == 'production' else False,
        samesite='Strict' if os.environ.get(
            'FLASK_ENV') == 'production' else None,
        httponly=True)
    return response


@app.route("/api/docs")
def api_help():
    """
    Returns all API routes and their doc strings
    """
    acceptable_methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    route_list = { rule.rule: [[ method for method in rule.methods if method in acceptable_methods ],
                    app.view_functions[rule.endpoint].__doc__ ]
                    for rule in app.url_map.iter_rules() if rule.endpoint != 'static' }
    return route_list


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def react_root(path):
    """
    This route will direct to the public directory in our
    react builds in the production environment for favicon
    or index.html requests
    """
    if path == 'favicon.ico':
        return app.send_from_directory('public', 'favicon.ico')
    return app.send_static_file('index.html')


@app.errorhandler(404)
def not_found(e):
    return app.send_static_file('index.html')
