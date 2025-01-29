# Flask Blueprints

Blueprints are extremely similar to `Router` from Express

Blueprint takes 3 arguments

- String to set the name of the blueprint
- `__name__` to specify the file name this blueprint is in
- `url_prefix=` set to the url path

Like with Express Router, any requests that start with `/spots` would go here

```py
# /app/routes/spots.py
from flask import Blueprint

bp = Blueprint('spots', __name__, url_prefix='/spots')

@bp.route('/pet-friendly')
def my_route():
    return render_template('pet_spots.html')
```

And any requests starting with `/reviews` will go here

```py
# /app/routes/reviews.py
from flask import Blueprint

bp = Blueprint('reviews', __name__, url_prefix='/reviews')

@bp.route('/5-star')
def my_route():
    return render_template('bribed-reviews.html')
```

All of your blueprints need to be connected to your app

`register_blueprint()` takes your blueprint, access through your module

```py
app.register_blueprint(routes.spots.bp)
app.register_blueprint(routes.reviews.bp)
```
