# Flask Routing

## `@app.route()` decorator

This be a decorator

Pass url string to `.route()`

## Wildcards

JS

- `/artist/:artistId`

PY

- `/artist/<artistId>`

Within `<>` is the variable name

**_REMINDER:_** a wildcard is **_NOT_** an indicator of what the user will put into their url

Flask allows wildcard typing, making it easier to direct users to the correct pages

Within `<>`, data type & colon, followed by route param

- `/artist/<int:artistId>`
  - `/artist/1` - 200
  - `/artist/A` - 404

To access the param, simply pass it to the route's function

```python
@app.route('/artist/<artistId>')
def artist_by_id(artistId):
  return f'<h1>Artist #{artistId}</h1>'
```

## Cool decorators

`@app.`

- `before_request`
- `after_request`
- `before_first_request`

## Built-in static

Remember how static files had to be served before? Pretty dumb

Flask has a dedicated `/static` route

- Store all static files inside a `static` folder
  - This should be inside whatever folder is running your app
- It's built in, no need to create a route for it!
