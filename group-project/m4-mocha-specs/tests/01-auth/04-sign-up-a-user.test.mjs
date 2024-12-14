import { expect, assert } from "chai";
import { apiBaseUrl } from "../utils/constants.mjs";
import {
  createUniqueUser,
  generateUniqueUsername,
} from "../utils/agent-helpers.mjs";
import {
  createManyAgents,
  fetchManyCsrfTokens,
} from "../utils/agent-factory.mjs";

describe("\nSign Up a User", function () {
  let agent,
    xsrfToken,
    agent2,
    xsrfToken2,
    agent3,
    xsrfToken3,
    agent4,
    xsrfToken4,
    userObj,
    userObj2;

  before(async function () {
    this.timeout(10000);
    userObj = createUniqueUser();
    userObj2 = createUniqueUser();
    [agent, agent2, agent3, agent4] = createManyAgents(apiBaseUrl, 4);
    [xsrfToken, xsrfToken2, xsrfToken3, xsrfToken4] = await fetchManyCsrfTokens([agent, agent2, agent3, agent4]);
  });

  describe("POST /api/users", function () {
    it("Correct Endpoint", function (done) {
      agent
        .post("/users")
        .send(userObj)
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken)
        .end(function (err, res) {
          if (err) return done(err);
          done();
        });
    });
  });

  describe("Response", function () {
    it("Status Code - 201", function (done) {
      agent2
        .post("/users")
        .send(createUniqueUser())
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken2)
        .expect(201)
        .end(function (err, res) {
          if (err) return done(err);
          done();
        });
    });

    it("Body Matches API Docs", function (done) {
      agent3
        .post("/users")
        .send(userObj2)
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken3)
        .end(function (err, res) {
          if (err) return done(err);

          const expected = {
            email: { value: userObj2.email, type: "string" },
            username: { value: userObj2.username, type: "string" },
            firstName: { value: userObj2.firstName, type: "string" },
            lastName: { value: userObj2.lastName, type: "string" },
          };

          Object.keys(expected).forEach((field) => {
            assert.strictEqual(
              res.body.user[field],
              expected[field].value,
              `${field} does not match`
            );
            assert.strictEqual(
              typeof res.body.user[field],
              expected[field].type,
              `Type of ${field} not as expected`
            );
          });
          assert.strictEqual(typeof res.body.user.id, "number");
          done();
        });
    });
  });
  
  describe("Error response: User already exists with the specified email or username", function () {
    it("Status Code - 500", function (done) {
      let userClone = { ...userObj };
      userClone.username = generateUniqueUsername();
      agent
        .post("/users")
        .send(userClone)
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken)
        .expect(500)
        .end(function (err, res) {
          if (err) return done(err);

          done();
        });
    });

    it("Error response: User already exists with the specified email", function (done) {
      let userClone = { ...userObj };
      userClone.username = generateUniqueUsername();
      agent
        .post("/users")
        .send(userClone)
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken)
        .end(function (err, res) {
          if (err) return done(err);
          assert.strictEqual(typeof res.body.errors.email, "string");

          done();
        });
    });

    it("Error response: User already exists with the specified username", function (done) {
      let userClone = { ...userObj };
      userClone.email = `${generateUniqueUsername()}@test.com`;
      agent
        .post("/users")
        .send(userClone)
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken)
        .end(function (err, res) {
          if (err) return done(err);
          expect(res.body).to.include.keys("message", "errors");
          expect(res.body.errors).to.include.keys("username");

          assert.strictEqual(typeof res.body.message, "string");
          assert.strictEqual(
            typeof res.body.errors.username,
            "string",
            "missing key [username]"
          );

          done();
        });
    });
  });

  describe("Error Response: Body validation errors", function () {
    it("Status Code - 400", function (done) {
      const incompleteUser = {
        firstName: "not-an-email",
      };
      agent4
        .post("/users")
        .send(incompleteUser)
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken4)
        .expect(400)
        .end(function (err, res) {
          if (err) return done(err);
          done();
        });
    });

    it("Body Matches API Docs", function (done) {
      const incompleteUser = {
        firstName: "not-an-email",
      };
      agent4
        .post("/users")
        .send(incompleteUser)
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken4)
        .end(function (err, res) {
          expect(res.body).to.have.property("message");
          expect(Object.keys(res.body.errors)).to.include(
            "username",
            "email",
            "lastName"
          );
          done();
        });
    });
  });
});
