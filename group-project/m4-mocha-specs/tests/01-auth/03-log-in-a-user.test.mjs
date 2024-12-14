import { expect, assert } from "chai";
import { apiBaseUrl } from "../utils/constants.mjs";
import {
  createAgent,
  fetchCsrfToken,
  agentSignUp,
} from "../utils/agent-factory.mjs";

describe("\nLog In a User", function () {
  let agent, xsrfToken, agentDetails;

  before(async function () {
    this.timeout(10000);
    agent = createAgent(apiBaseUrl);
    xsrfToken = await fetchCsrfToken(agent);
    let res = await agentSignUp(agent, xsrfToken);
    agentDetails = res.body.user;

  });

  describe("POST /api/session", function () {
    it("Correct Endpoint", function (done) {
      agent
        .post("/session")
        .send({ credential: agentDetails.email, password: "secret password" })
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken)
        .end(function (err, res) {
          if (err) return done(err);
          done();
        });
    });
  });

  describe("Response", function () {
    it("Status Code - 200", function (done) {
      agent
        .post("/session")
        .send({ credential: agentDetails.email, password: "secret password" })
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken)
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
        .expect((response) => {
          if (!("user" in response.body))
            throw new Error("Missing key in response");
          if (!("firstName" in response.body.user))
            throw new Error("Missing key in response");
          if (!("email" in response.body.user))
            throw new Error("Missing key in response");
        })

        .end(function (err, res) {
          if (err) return done(err);
          const expected = {
            email: { value: agentDetails.email, type: "string" },
            username: { value: agentDetails.username, type: "string" },
            firstName: { value: agentDetails.firstName, type: "string" },
            lastName: { value: agentDetails.lastName, type: "string" },
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

  describe("Error Response: Invalid credentials", function () {
    it("Status Code - 401", function (done) {
      agent
        .post("/session")
        .send({ credential: agentDetails.email, password: "no" })
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken)
        .expect(401)
        .end(function (err, res) {
          if (err) return done(err);
          done();
        });
    });

    it("Body Matches API Docs", function (done) {
      agent
        .post("/session")
        .send({ credential: agentDetails.email, password: "no" })
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken)
        .end(function (err, res) {
          if (err) return done(err);
          expect(err).to.not.exist;
          expect(res.body).to.have.property("message");

          expect(res.body.message).to.equal("Invalid credentials");
          done();
        });
    });
  });

  describe("Error Response: Body validation errors", function () {
    it("Status Code - 400", function (done) {
      agent
        .post("/session")
        .send({ credential: "", password: "" })
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken)
        .expect(400)
        .end(function (err, res) {
          if (err) return done(err);
          done();
        });
    });

    it("Body Matches API Docs", function (done) {
      agent
        .post("/session")
        .send({ credential: "", password: "" })
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken)
        .end(function (err, res) {
          if (err) return done(err);
          expect(err).to.not.exist;
          expect(res.body).to.have.property("message");
          expect(res.body.message).to.equal("Bad Request");
          done();
        });
    });
  });
});
