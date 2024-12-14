# M4 Mocha Tests 🚀

This repo contains a test suite for the M4 project.

## Quick Start

- Run: `npm install`.
- Update the base url in [`test/utils/constants`](./tests/utils/constants.mjs) ⭐
- Run: `npm test`.

## Running the Tests

To get the tests working, ensure you've configuired the following:

- Update the base url to point to your live site on Render or your server running on localhost:8000.
- Ensure your server is running, or your live site is up and running.
- [`test/utils/constants`](./tests/utils/constants.mjs) is the only place you'll need to make a change.

Use `npm test` to run all of the tests.  The test results will map 1-to-1 with your Scorecard.

## General Tips to Debug Failing Tests

  - You can console.log in your route handlers, and then run the tests to see what's going on in your express app.
  - You can also add console.logs directly inside of the test suite.
