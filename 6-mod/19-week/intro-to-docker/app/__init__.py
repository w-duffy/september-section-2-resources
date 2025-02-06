from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/hello")
def hi():
    return "Hello cool!"

@app.route("/api/reviews")
def get_reviews():
    return {"Reviews": [{"id": 1, "rev": "some rev"}]}
