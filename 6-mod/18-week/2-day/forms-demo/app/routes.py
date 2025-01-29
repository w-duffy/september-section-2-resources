from flask import Blueprint, render_template

from app.form import QuickForm



# spots = Blueprint("spots", __name__, url_prefix="/spots")
spots = Blueprint("spots", __name__, url_prefix="/spots")

@spots.route("/")
def all_spots():
    """Get all spots"""
    return {"Spots": "spots"}, 200


reviews = Blueprint("reviews", __name__)

@reviews.route("/")
def all_reviews():
    """Get all reviews"""
    return {"reviews": "reviews"}, 200






















bp = Blueprint("test", __name__, url_prefix="/test")


@bp.route("/")
def main():
    test_info = {"title": "This is the test route", "heading": "Test route!"}
    return render_template("page.html", info=test_info)


@bp.route("/form", methods=["GET", "POST"])
def form():
    form = QuickForm()
    if form.validate_on_submit():
        print(dir(form))
        print("\n----\n")
        print(form.age)
        print("\n----\n")
        print(form.csrf_token)
        print("\n----\n")
        print(form.data)
        print("\n----\n")
        print(form.errors)
        print("\n----\n")
        print(form.hidden_tag())
        print("\n----\n")
        print(form.name)
        print("\n----\n")
        print(form.submit)
        print("\n----\n")
        print(form.validate_on_submit())
        return "Form submitted!"
    info = {"title": "Form page", "heading": "Form route"}
    return render_template("page.html", form=form, info=info)
