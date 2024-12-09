# RESTful API Endpoints

In this reading, you will learn how to create endpoints that follow the RESTful
convention for a JSON web API server.

## RESTful Convention for web API Servers

Web API servers only need to return and manipulate data. Instead of interacting
with the data through HTML web pages like in a traditional HTML web server,
developers can make requests to a web API server to read and manipulate data.
Therefore, there is no need for a HTML web pages to be displayed or returned
from a web API server. That means there is no need for `GET` endpoints for
viewing the HTML form pages on a web API server.

A web API server is not limited to just `GET` and `POST` requests like a
traditional HTML web server is. A web API server should be able to accept all
methods (`GET`, `POST`, `PUT`/`PATCH` and `DELETE`) in a request.

The following tables show the paths and HTTP verbs used to interact with
JSON-based versions of a RESTful application:

| Path Pattern             | HTTP Verb | Meaning                                          |
| ------------------------ | --------- | ------------------------------------------------ |
| /resource-name           | GET       | Index: Get all of the records for the resource   |
| /resource-name           | POST      | Create: Create a new record for the resource     |
| /resource-name/record-id | GET       | Details: Get the details of the specified record |
| /resource-name/record-id | PUT/PATCH | Update: Update the specified record              |
| /resource-name/record-id | DELETE    | Delete: Delete the specified record              |

For Nested Resources:

| Path Pattern                             | HTTP Verb | Meaning                                                                                |
| ---------------------------------------- | --------- | -------------------------------------------------------------------------------------- |
| /resource-name/record-id/nested-resource | GET       | Index: Get all of the records for the nested resources related to the specified record |
| /resource-name/record-id/nested-resource | POST      | Create: Create a new record for the nested resource related to the specified record    |
| /nested-resource/nested-record-id        | GET       | Details: Get the details of the specified nested resource's record                     |
| /nested-resource/nested-record-id        | PUT/PATCH | Update: Update the specified nested resource's record                                  |
| /nested-resource/nested-record-id        | DELETE    | Delete: Delete the specified nested resource's record                                  |

### Twitter RESTful endpoints example

Using a Twitter application as an example, the following table describes
different RESTful endpoints for a collection of tweets.

| HTTP Verb | Meaning                              | With respect to **/my/tweets** |
| --------- | ------------------------------------ | ------------------------------ |
| GET       | Get "all" of the specified resources | Get all of your tweets         |
| POST      | Create a new resource                | Create a new tweet             |
| PUT       | n/a                                  | n/a                            |
| PATCH     | n/a                                  | n/a                            |
| DELETE    | Delete all of the resources          | Delete all of your tweets      |

The following table describes different RESTful endpoints for a single tweet
record.

| HTTP Verb | Meaning                         | With respect to **/my/tweets/17**                       |
| --------- | ------------------------------- | ------------------------------------------------------- |
| GET       | Get the details of the resource | Get that specific tweet with id 17                      |
| POST      | n/a                             | n/a                                                     |
| PUT       | Replace the resource            | Replace all of the tweet details with the provided data |
| PATCH     | Update the resource             | Update specific properties of the tweet                 |
| DELETE    | Delete the specified resource   | Delete that specific tweet                              |

### Current weather example

In another example, consider the path that reads **/weather/current**. That
doesn't point to any static single record in the weather database. Instead, it
would return the _most recent_ record of weather in the database. The id of
"current" would be treated special and initiate a lookup of the most recent
record rather than a specific record like **/weather/10392**.

## GitHub API example

GitHub has a much vaunted RESTful API that many people use as a model for how to
do _good API design_. This section checks out some of its features.

First, check out this [GitHub REST API endpoint] for a GET request to the
`app-academy` user and the endpoint's response below. Notice how the information
is formatted as JSON. JSON is the preferred format over other formats like XML.
Feel free to take a look at the [GitHub API documentation] for sending a GET
request for a single user.

If your browser is rendering the JSON below without the quotes around the
property names, you're likely using the extension [JSONView] to _prettify_
your JSON in JavaScript. The [JSONView] extension _prettifies_ JSON by parsing
the JSON text data into a JavaScript object. Note that you can also parse JSON
into JavaScript by using the `JSON.parse()` method. Another extension, [JSON
Viewer], also _prettifies_ JSON but it correctly preserves the quotes around the
property names.

If you opened https://api.github.com/users/app-academy endpoint in your browser,
you should see the JSON formatted data below.  Feel free to navigate to the
links in the JSON.

```json
{
  "login": "app-academy",
  "id": 3155975,
  "node_id": "MDQ6VXNlcjMxNTU5NzU=",
  "avatar_url": "https://avatars0.githubusercontent.com/u/3155975?v=4",
  "gravatar_id": "",
  "url": "https://api.github.com/users/app-academy",
  "html_url": "https://github.com/app-academy",
  "followers_url": "https://api.github.com/users/app-academy/followers",
  "following_url": "https://api.github.com/users/app-academy/following{/other_user}",
  "gists_url": "https://api.github.com/users/app-academy/gists{/gist_id}",
  "starred_url": "https://api.github.com/users/app-academy/starred{/owner}{/repo}",
  "subscriptions_url": "https://api.github.com/users/app-academy/subscriptions",
  "organizations_url": "https://api.github.com/users/app-academy/orgs",
  "repos_url": "https://api.github.com/users/app-academy/repos",
  "events_url": "https://api.github.com/users/app-academy/events{/privacy}",
  "received_events_url": "https://api.github.com/users/app-academy/received_events",
  "type": "User",
  "site_admin": false,
  "name": null,
  "company": null,
  "blog": "",
  "location": null,
  "email": null,
  "hireable": null,
  "bio": null,
  "public_repos": 2,
  "public_gists": 1,
  "followers": 3,
  "following": 0,
  "created_at": "2012-12-31T00:08:43Z",
  "updated_at": "2016-02-27T05:27:57Z"
}
```

Navigate to the JSON's [followers_url] and [repos_url]. Notice how the url path
of those endpoints connect to the endpoint that fetches all the data connected
to the `app-academy` user.

Now open the [followers_url] endpoint in your browser. You are now sending a
`GET` request to GitHub's server to receive an array of followers associated to
the `app-academy` user. Keep in mind that there are many [Public APIs] available
as you plan your first full-stack project next week.

## What you learned

In this article, you covered quite a bit. You learned that

[GitHub REST API endpoint]: https://api.github.com/users/app-academy
[GitHub API documentation]: https://developer.github.com/v3/users/#get-a-single-user
[JSON Viewer]: https://chrome.google.com/webstore/detail/json-viewer/gbmdgpbipfallnflgajpaliibnhdgobh
[JSONView]: https://chrome.google.com/webstore/detail/jsonview/chklaanhfefbnpoihckbnefhakgolnmc
[followers_url]: https://api.github.com/users/app-academy/followers
[repos_url]: https://api.github.com/users/app-academy/repos
[Public APIs]: https://github.com/public-apis/public-apis
