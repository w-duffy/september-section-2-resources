# Microservices Project Overview

Today's project will have two parts. First, you will Dockerize a data-driven
Express app that serves HTML to show book listings. You will fetch and render
books that have been seeded in a Postgres database. Second, you will make a
data-driven Flask microservice that handles averaging star ratings (and the POST
requests to record new ratings). Instead of extending your Express app as a
monolith, you'll build a Flask app as a separate microservice that tracks book
ratings. 

The goal for your Flask app is to create a microservice that manages the
submission and averaging of book ratings. After creating the microservice, you
will implement it into your Express app! Since you'll Dockerize your Express app
for local development, you'll run and track your local changes for the app
within a container.

Here is a general breakdown of the features that each service should have at the
end of the project:

* Express app: Book Listings
  * Home page that renders a list of books
  * Forms and routes to create, edit, and delete books
  * Form to create a rating using the microservice
  * Rating show page that renders a book's ratings and details

* Flask app: Book Ratings
  * `POST title/user-ratings` microservice endpoint to post a user's rating.
  * `GET title/user-ratings` microservice endpoint that queries, averages, and
    sends all the rating information of a book from the database.
