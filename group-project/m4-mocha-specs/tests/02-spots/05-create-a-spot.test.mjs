import { expect } from "chai";
import { apiBaseUrl } from "../utils/constants.mjs";
import { createUniqueSpot } from "../utils/agent-helpers.mjs";
import { expectedNeOrEditSpotKeys } from "../utils/err-helpers.mjs";
import {
  agentCreateSpot,
  agentSignUp,
  agentCreateSpotImage,
  fetchManyCsrfTokens,
  createManyAgents,
} from "../utils/agent-factory.mjs";


describe("\nCreate a Spot", function () {
  let agent, xsrfToken, agentSpot, agent2, xsrfToken2, agentNonAuth, xsrfToken3;

  before(async function () {
    this.timeout(15000);
    [agent, agent2, agentNonAuth] = createManyAgents(apiBaseUrl, 3);
    [xsrfToken, xsrfToken2, xsrfToken3] = await fetchManyCsrfTokens([agent, agent2, agentNonAuth]);


    await agentSignUp(agent, xsrfToken);
    let res = await agentCreateSpot(agent, xsrfToken);
    agentSpot = res.body;
    let imageRes = await agentCreateSpotImage(agent, xsrfToken, agentSpot.id);
    agent.image = imageRes;
  });

  describe("POST /api/spots", function () {
    it("Correct Endpoint", function (done) {
      const spotData = createUniqueSpot();
      agent2
        .post("/spots")
        .send(spotData)
        .set("X-XSRF-TOKEN", xsrfToken2)
        .set("Accept", "application/json")
        .end(function (err, res) {
          expect(err).to.not.exist;
          done();
        });
    });

    it("Authentication", function (done) {
      const spotData = createUniqueSpot();
      agentNonAuth
        .post("/spots")
        .set("X-XSRF-TOKEN", xsrfToken3)
        .send(spotData)
        .set("Accept", "application/json")
        .expect(401)
        .end(function (err, res) {
 if (err) return done(err);
 done();
        });
    });
  });
  describe("Response", function () {
    it("Status Code - 201", function (done) {
      const spotData = createUniqueSpot();
      agent
        .post("/spots")
        .send(spotData)
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken)
        .expect(201)
        .end(function (err, res) {
          expect(err).to.not.exist;
          done();
        });
    });

    it("Body Matches API Docs", function (done) {
      const spotData = createUniqueSpot();
      agent
        .post("/spots")
        .send(spotData)
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken)
        .expect("Content-Type", /json/)
        .end(function (err, res) {
          expect(err).to.not.exist;
          expect(res.body).to.include.keys(expectedNeOrEditSpotKeys);
          expect(res.body.name).to.equal(spotData.name);
          expect(res.body.address).to.equal(spotData.address);
          done();
        });
    });
  });
  describe("Error Response", function () {
    it("Status Code - 400", function (done) {
      const incompleteData = {
        city: "San Francisco",
        state: "California",
        country: "United States of America",
      };

      agent
        .post("/spots")
        .send(incompleteData)
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken)
        .expect(400)
        .end(function (err, res) {
          if (err) return done(err);
          done();
        });
    });

    it("Body Matches API Docs", function (done) {
      const incompleteData = {
        city: "San Francisco",
        state: "California",
        country: "United States of America",
      };

      agent
        .post("/spots")
        .send(incompleteData)
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken)
        .end(function (err, res) {
          expect(res.body).to.have.property("message");
          expect(res.body.errors).to.include.all.keys(
            "address",
            "lat",
            "lng",
            "name",
            "description",
            "price"
          );
          if (err) return done(err);
          done();
        });
    });
  });
});
