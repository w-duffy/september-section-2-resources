# Templating With Jinja

Main reasons to use templating

- "Easier"
  - If you understand the template language very well, it's easier
  - A complex React App's html can be messier than using templates
- Lightweight
  - Much easier to run than a React App
  - Generally used for internal tools, in development, etc
    - You wouldn't book a flight to a place you can walk to
    - You shouldn't build a React App for a task you can template
- You might see it somewhere in the real world
  - Might not be Jinja, but templating is very similar across many implementations
- Not really any other reasons to use templates
  - If the above cases don't apply, use React!

## Works with Flask right out the box

`render_template` built-in function in Flask package

```py
from flask import render_template
from flask import Flask, render_template
```

Expects that all templates are in a "templates" folder

Pass filename to function to render that template

- Will automatically look in your "templates" folder

```py
@app.route('/')
def index():
    return render_template('index.html')
```

## Jinjariables

We can use variables through double curly braces `{{ variable_name }}`

Pass as kwarg to `render_template` and used inside your templates

Works just like props!

```py
res = # Pretend database stuff happens here
return render_template('index.html', user=res.first_name)
```

```html
<!-- /app/templates/index.html -->
<!DOCTYPE html>
<html>
  <head>
    <h1>Hello {{ user }}!</h1>
  </head>
</html>
```

## Jinjitionals

Put conditionals right into html

```html
{% if not logged_in %}
<a href="/login">Log in</a>
{% endif %}
```

## Jinjeration

```py
nav = [
  { 'href': 'https://appacademy.io', 'caption': 'App Academy' },
  { 'href': 'https://web.archive.org/', 'caption': 'Internet Archive' },
]

render_template("page.html", nav=nav)
```

```html
<ul>
  {% for el in nav %}
  <li>
    <a href="{{ el.href }}">{{ el.caption }}</a>
  </li>
  {% endfor %}
</ul>
```

## Jinjonents

You can break your templates into React-like "components" by simply making more template files

Then, combine using the `include` keyword

```html
<!-- /app/templates/other_page.html -->
<h2>This sure is some other page!</h2>

<!---->
<!---->
<!---->

<!-- /app/templates/index.html -->
<!DOCTYPE html>
<html>
  <head>
    <h1>Hello {{ user }}!</h1>
    {% include 'other_page.html' %}
  </head>
</html>
```
