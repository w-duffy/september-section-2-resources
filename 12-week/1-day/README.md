# Serving Static Files

## Static vs Dynamic

- Dynamic: handling a request through app.methodName(), "manually" deciding what happens
- Static: serving a file "as-is"

In express, we can serve static files using `express.static`

```js
express.static('locationOfTheFile');
```

To tell our app to use this:

```js
app.use(path, express.static('locationOfTheFile'));
// or
app.use(express.static('locationOfTheFile'));
```

Passing no path to `app.use()` will have the file be served from the root of the url, ie. localhost:5000

If we specify a path, the files from `express.static()` will be served from that path in the url, regardless of where they actually are in the file.

This works similarly to express routers!

```md
# File structure

-space
--- milkyWay.js
--- earth
------- climateChange.js
```

```js
app.use('/earth', express.static("space"))

GET localhost:5000/earth/milkyWay.js // 200
GET localhost:5000/earth/climateChange.js // 404
```

## Using an absolute path for production

When your application is ready for production, you can't be 100% sure the express server will launch from within your application. This will cause our file paths to get messed up.

Thankfully, we can use an _absolute path_

```js
const path = require('path');

app.use('/earth', express.static(path.join(__dirname, 'space')));
```

We will need to import `path`, which is available to us by default in Node (so no npm install required). Then we join our file's path to `__dirname`, which is just the folder that the server starts in.
