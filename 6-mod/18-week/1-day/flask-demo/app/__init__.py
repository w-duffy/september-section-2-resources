from flask import Flask, render_template

from .config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route("/")
def index():
    nav = [
        {"href": "https://appacademy.io", "caption": "App Academy"},
        {"href": "https://web.archive.org/", "caption": "Internet Archive"},
    ]
    return render_template("index.html", title="Home", logged_in=True, nav=nav)


# @app.route("/other")
# def other():
#     return render_template("index.html", title="Other", logged_in=False)


# ! ----------------------------------------------------------------------------
# * ----- Pre-jinja flask
# ! ----------------------------------------------------------------------------

# @app.route("/")
# def index():
#     return """
# <h1>Yo whats up? This kinda sucked so far</h1>
# <h1>Yo whats up? This kinda sucked so far</h1>
# <h1>Yo whats up? This kinda sucked so far</h1>
# <h1>Yo whats up? This kinda sucked so far</h1>
# <h1>Yo whats up? This kinda sucked so far</h1>
# """


# @app.route("/hello")
# def hello():
#     return "Hey there stranger"


# @app.route("/hello/<string:name>/<int:age>")
# def hello_name(age, name):
#     print(type(age))
#     print(type(name))
#     return f"Hey there {name}, you're {age} years old"


# @app.route("/hello/<val>")
# def hello_val_any(val):
#     print(type(val))
#     return f"Hey there {val}"


# @app.route("/hello/<int:val>")
# def hello_val_num(val):
#     print(type(val))

#     return f"Hey there number {val}"
