
# Group Project -- Grading and Bugs Squashing


## Grading

Mocha Specs to test your endpoints
- https://github.com/w-duffy/september-section-2-resources/tree/main/group-project/m4-mocha-specs

When all of your mocha specs are passsing, you can submit your project and have it scored via the instructions in the repo below.  This repo uses the mocha specs.
- https://github.com/w-duffy/m4-project-grading


##  Common Bugs and a Potential Solution

1. Not passing `options` to the migration and seeder files.
  - You can reference the examples in Auth Me to see how to do this for all of your seeders and migrations.
  - [Adding `options` to your migration](https://github.com/appacademy/aa12-authenticate-me/blob/full-time/README-backend-phase-3.md#users-table-migration)
  - [Adding `options` to your seeders](https://github.com/appacademy/aa12-authenticate-me/blob/full-time/README-backend-phase-3.md#user-seeds)

2. Stale data in your production database that conflicts with the latest changes you made locally.
  - To fix this, use psql to drop your `SCHEMA` on your Render database: [How to Drop your SCHEMA](https://scribehow.com/shared/How_to_Drop_Your_SCHEMA_in_Render__pz5X9Ck6QG-OXN78rXVqEw).
  - You can also delete your existing infrastructure on Render, and create a new PostgreSQL database and Web Service.
  - Double check that you've followed every step in the [deployment reading](https://github.com/appacademy/aa12-authenticate-me/blob/full-time/README-deploy.md).

3. Debugging failing mocha specs.
  - You can console.log in your route handlers, and then run the tests to see what's going on.
  - You can also add console.logs directly inside of the test suite.  Here are a couple of threads where a team resolved mocha specs that they weren't originally passing:
