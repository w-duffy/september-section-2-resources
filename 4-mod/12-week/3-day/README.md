# Let's face our insecurities 😌

## We can't be trusted with this power

- You will not be in charge of security for the teams you join
- Our role is to be aware of potential security vulnerabilities

## So like why do I even care?

- Websites store important data
- Data breaches can be costly for us/our employers
- Malicious actors might try to break/take down our apps

## Short list of types of attacks

- SQL injections
- Cross-site Scripting (XSS)
- Remote File Inclusion
- Cross-site Request Forgery (CSRF)

## CORS

- CORS is an acronym, it stands for Cross-Origin Resource Sharing
- It allows servers to indicate valid sources (origins) from which resources may be loaded on the browser
- We can set the policy on the server side (backend), but it is enforced on the frontend by the browser
- Express does not support CORS by default, we have to set that up ourselves:
  - `npm install cors`

```js
// app.js
// Import the CORS package
const cors = require('cors');

// ... Server setup

// Use CORS in your application
app.use(
  cors({
    origin: ['http://example1.com', /\.example2\.com$/], // Array of allowed domains
  })
);
```

## XSS

- XSS stands for Cross-site scripting
  - Refers to the injection and execution of JavaScript into the HTML of an application
- These scripts can perform anything available within browser JavaScript
- Here you won't be asked to implement any security measures against XSS attacks from scratch
  - Down the line, you will use third-party libraries to perform security checks for you

## CSRF

1. Server sends 2 tokens
2. User sends both tokens BACK TO SERVER on every request
3. Server verifies that the 2 tokens match

- If they match, request is fulfilled
- If they don't, request is denied
