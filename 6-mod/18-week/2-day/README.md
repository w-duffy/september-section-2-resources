# Tonight's HW on SQLAlchemy

Don't focus too hard on the setup instructions from the first few readings

- We start off showing you how to use SQLAlchemy _without_ Flask

- However, we only ever use them together, so the syntax will be different

The final reading today and the 3 lecture videos showcase the relevant syntax

- This is the syntax you'll be using in your projects and on the assessment!

## DB Setup

The videos reference setting up your database through PostgreSQL

Since we're using SQLite3, the setup is slightly different

In our `.env` file, we set our db url to be our local sqlite file

- The filename should match the filename in your application!

```zsh
DATABASE_URL=sqlite:///dev.db
```
