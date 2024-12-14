import { assert } from "chai";
import { apiBaseUrl } from "../utils/constants.mjs";
import {
  createManyAgents,
  agentSignUp,
  fetchManyCsrfTokens,
} from "../utils/agent-factory.mjs";

describe("\nGet the Current User", function () {
  console.log("\x1b[32m%s\x1b[0m", "\nWelcome to the test suite!", "👋");
  console.log("\x1b[31m%s\x1b[0m", "\nPlease provide any feedback regarding bugs!", "🐛");
  console.log("\x1b[32m%s\x1b[0m", "\nRemember to wake up Render before running `npm test`", "🌟");
  let agent, newAgent, xsrfToken, xsrfToken2, agentDetails;

  before(async function () {
    this.timeout(10000);
    [agent, newAgent] = createManyAgents(apiBaseUrl, 2);
    [xsrfToken, xsrfToken2] = await fetchManyCsrfTokens([agent, newAgent]);
    let res = await agentSignUp(agent, xsrfToken);
    agentDetails = res.body.user;
  });

  describe("GET /api/session", function () {
    it("Correct Endpoint", function (done) {
      newAgent
        .get("/session")
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken2)
        .expect("Content-Type", /json/)
        .end(function (err, res) {
          if (err) return done(err);
          done();
        });
    });
  });

  describe("Successful Response when there is a logged in user", function () {
    it("Status Code - 200", function (done) {
      newAgent
        .get("/session")
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken2)
        .expect(200)
        .end(function (err, res) {
          if (err) return done(err);
          done();
        });
    });

    it("Body Matches API Docs", function (done) {
      agent
        .post("/session")
        .send({ credential: agentDetails.email, password: "secret password" })
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken)
        .end(function (err, res) {
          if (err) return done(err);

          const expected = {
            email: { value: agentDetails.email, type: "string" },
            username: { value: agentDetails.username, type: "string" },
            firstName: { value: agentDetails.firstName, type: "string" },
            lastName: { value: agentDetails.lastName, type: "string" },
            id: { value: agentDetails.id, type: "number" },
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
          done();
        });
    });
  });

  describe("Successful Response when there is no logged in user", function () {
    it("Status Code - 200", function (done) {
      newAgent
        .get("/session")
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken)
        .expect(200)
        .expect("Content-Type", /json/)
        .end(function (err, res) {
          if (err) return done(err);
          done();
        });
    });

    it("Body Matches API Docs", function (done) {
      newAgent
        .get("/session")
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken)
        .expect("Content-Type", /json/)
        .expect((response) => {
          if (!("user" in response.body)) throw new Error("Missing key user");
          if (response.body.user !== null)
            throw new Error("Missing key in response");
        })
        .end(function (err, res) {
          if (err) return done(err);
          assert.strictEqual(res.body.user, null);
          done();
        });
    });
  });
});
