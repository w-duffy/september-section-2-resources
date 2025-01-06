# Converting Function Components

In this short practice you will convert a `function` component into a `class`
component.

## Setup

Clone the starter repo, which you can access through the `Download Project`
button at the bottom of this page.

`cd` into the practice's root directory and run `npm install`. To start your
app, run `npm run dev`.

## Create a class component

In the __src/components__ directory, create a __ClassComponentOne.js__ file that
you will use to define your first class component.

To create a class component, you must first import the
[`Component`][react-component] class from the `react` package, which your
component will inherit from. This will give your component access to the
`setState` method, among other things.

Create a class component called `ClassComponentOne` that extends the imported
`Component` class.

```jsx
// src/components/ClassComponentOne.jsx

import { Component } from 'react';

class ClassComponentOne extends Component {

}
```

Class components must always have a render method:

```jsx
// src/components/ClassComponentOne.jsx

//...
class ClassComponentOne extends Component {
  render() {

  }
}
```

Inside the render method, you must return JSX or some other render-able value
such as `null`, just as you do in function components.

Copy the whole `return` from the `FunctionComponentOne` component. Paste it
inside the `render` method within `ClassComponentOne`.

Change the `h1` text from `Function Component One` to `Class Component One`.

You access and update state differently in class components than in function
components. So for now, give each `onClick` and `onChange` handler an empty
function body, and replace each reference to `message` and `count` with
`undefined`. You will be recreating these shortly.

Finally, remember to import the `FunctionComponentTwo` component that will
now be the child of this component.

Your code should look something like this:

```jsx
// src/components/ClassComponentOne.jsx

import { Component } from 'react';
import FunctionComponentTwo from './FunctionComponentTwo';

class ClassComponentOne extends Component {
  render() {
    return (
      <div className='center'>
        <h1>Class Component One</h1>
        <div className='one'>
          <button onClick={(e) => {}}>
            Decrement
          </button>
          <button onClick={(e) => {}}>
            Increment
          </button>

          <input
            type='text'
            value={undefined}
            onChange={(e) => {}}
            placeholder='Enter Your Message'
          />
          <button onClick={() => {}}>Clear</button>
        </div>

        <FunctionComponentTwo count={undefined} message={undefined} />
      </div>
    );
  }
}
```

Export your class component as the `default` export, then import it within
__src/App.jsx__ and render it within your `App` instead of
`FunctionComponentOne`.

You should see your new `ClassComponentOne` on the page. However, it's not
interactive yet; that comes next!

## Initializing State

Look in the __src/components/FunctionComponentOne.jsx__ file and notice the two
slices of state. [State] in a class component is represented by one single
object. Each key inside the object represents a slice of state. The initial
value for each slice of state is the value you set for that key when
initializing the `state` object.

You should initialize your state inside your component class's `constructor`.

Above the `render` method in __ClassComponentOne.js__, create a `constructor`
function with a parameter of `props`. **You must include `super(props)` at
the top of your `constructor`** since the `constructor` from the `Component`
superclass does some important setup work.

After `super(props)`, initialize `state` by assigning a plain JavaScript object
to `this.state`. **This is the only time you should ever assign anything
directly to `this.state`.**

Using the initial values you pass to `useState` in `FunctionComponentOne`,
create key/value pairs for `count` and `message` in your `this.state` object.

Your constructor should now resemble the code below:

```js
constructor(props){
  super(props);
  this.state = {
    count: 0,
    message: ''
  };
}
```

## Setting State

To update state in event handlers or anywhere else, class components use the
method [`this.setState`][setstate]. **Never try to update state by mutating
`this.state`!** React will only know to re-render your component if
`this.setState` is invoked.

`this.setState` takes an object that needs only the key/value pairs you wish to
change. React merges those updates using a *shallow merge*. Only the key/value
pairs that are passed to `this.setState` will change.

In the `message` input's `onChange` event handler, call `this.setState`. Pass in
an object with a key of `message` (i.e., the slice of state you're updating)
pointing to the `value` of the synthetic event's `target` element.

## Previous State

Remember the optional function provided for updating `state` that is based on
previous state? An optional function can also be provided to the `setState`
method. However, this function must return an object. See if you can figure out
the syntax for making that happen with the `Increment` and `Decrement` buttons.

Next, define an `onClick` event handler on the `Clear` button so that it clears
the `message` slice of state.

Your code for event handlers should look similar to the code below:

```jsx
<button
  onClick={() => {
    this.setState(prevState => ({
      count: prevState.count - 1
    }));
  }}
>
  Decrement
</button>
<button
  onClick={() => {
    this.setState(prevState => ({
      count: prevState.count + 1
    }));
  }}
>
  Increment
</button>
<input
  type='text'
  value={undefined}
  onChange={e => this.setState({ message: e.target.value })}
  placeholder='Enter Your Message'
/>
<button onClick={() => this.setState({ message: '' })}>Clear</button>
```

## Referencing State

To retrieve values in `state`, you must reference the `this.state` property of
your component instance. From there, you can key into individual slices of
state.

Using this information, set the `value` for the `message` input. Set the
two props that are being passed to `FunctionComponentTwo` as well.

## Defining Event Handlers as Methods

Instead of defining your event handlers as inline arrow functions, you may want
to define them as methods of your class. There are several reasons you might
want to do this: to make your event handlers reusable, to separate your
component logic from your JSX, etc.

However, you need to be careful about context (i.e., what `this` refers to).
Consider the following example:

```jsx
handleClick(event) {
  this.setState({ message: 'oh no' });
}

render() {
  return <button onClick={this.handleClick}>Uh Oh</button>
}
```

When you click the rendered button, `this.handleClick` will be invoked. However,
being a callback, it will be invoked function-style. As a result, it loses its
context; `this` won't refer to the component instance anymore.
`this.setState` will then no longer be defined, so you will get an error
that your app `Cannot read properties of undefined (reading 'setState')`.

There are three approaches to ensuring `this` in event handlers appropriately
points to the component instance.

### Approach 1: Bind the event handler in `constructor`

The goal with this approach is to override `this.handleClick` in your
constructor so that it points to a bound version of the `handleClick` method.

```js
constructor(props){
  this.handleClick = this.handleClick.bind(this);
}

handleClick(event) {
  this.setState({ message: 'yay! `this` points to the component instance!' });
}
```

Now, you can set `onClick={this.handleClick}` without worrying about losing
context.

### Approach 2: Invoke the event handler in an arrow function

Instead of passing `this.handleClick` directly as the event handler, you can
instead supply an inline arrow function that then invokes `handleClick` on
`this`:

```jsx
<button onClick={(e) => this.handleClick(e)} />
```

Inside the arrow function callback, `this` still refers to the component, since
arrow functions don't set their own `this`. You then call `this.handleClick`
method-style, thus preserving context.

### Approach 3: Use experimental `class fields` syntax

Lastly, you can use the [`public class fields`] syntax.

Setting a public class field looks like setting a variable within the class
definition, but outside any method; the difference is that you omit `let` or
`const`. This will then become a property of each instance:

```js
class Foo {
  bar = 'this is a public class field'
}

let f = new Foo();
console.log(f.bar); // => 'this is a public class field'
```

By assigning an arrow function to a public class field, you are essentially
defining a method for which `this` always refers to the instance:

```js
class Foo {
  bar = 'this is a public class field'
  sayBar = () => console.log(this.bar)
}

let f = new Foo();
f.sayBar(); // => 'this is a public class field'
```

For more on responding to events, see the [React docs][event-handling].

### Adding an alert button

Choose your favorite approach for preserving context in event handlers; the
examples below use public class fields.

Below the `Clear` button, add the following button:

```jsx
<button
  className='alert-button'
  onClick={this.handleClick}
>
  Alert
</button>
```

Next, define a `handleClick` method that calls `alert(this.state.message)`:

```jsx
// ... 
handleClick = () => {
  alert(this.state.message);
};

render() {
  // ...
}
```

Test that this is working. Hurrah!

## What you have learned

**Congratulations!** In this practice you have learned how to

1. Create a class component
2. Convert a function component to a class component
3. Initialize state by assigning to `this.state` in the `constructor`
4. Update state using the `this.setState` method
5. Preserve context in event handlers

[react-component]: https://react.dev/reference/react/Component
[setstate]: https://react.dev/reference/react/Component#setstate
[State]: https://react.dev/reference/react/Component#state
[event-handling]: https://react.dev/learn/responding-to-events
[`public class fields`]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Public_class_fields
