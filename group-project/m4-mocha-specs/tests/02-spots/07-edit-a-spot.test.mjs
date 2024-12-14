import { expect } from "chai";
import { apiBaseUrl } from "../utils/constants.mjs";
import { createUniqueSpot } from "../utils/agent-helpers.mjs";
import { expectedNeOrEditSpotKeys } from "../utils/err-helpers.mjs";
import {
  agentCreateSpot,
  agentSignUp,
  agentCreateSpotImage,
  createManyAgents,
  fetchManyCsrfTokens,
} from "../utils/agent-factory.mjs";

describe("\nEdit a Spot", function () {
  let agent, xsrfToken, agentSpot, agent2, xsrfToken2, agentNonAuth, xsrfToken3;

  before(async function () {
    this.timeout(15000);
    [agent, agent2, agentNonAuth] = createManyAgents(apiBaseUrl, 3);
    [xsrfToken, xsrfToken2, xsrfToken3] = await fetchManyCsrfTokens([agent, agent2, agentNonAuth]);
    await agentSignUp(agent, xsrfToken);
    await agentSignUp(agent2, xsrfToken2);
    let res = await agentCreateSpot(agent, xsrfToken);
    agentSpot = res.body;
    let imageRes = await agentCreateSpotImage(agent, xsrfToken, agentSpot.id);
    agent.image = imageRes;
  });

  describe("PUT /api/spots/:spotId", function () {
    it("Correct Endpoint", function (done) {
      let validSpotId = agentSpot.id;
      const spotData = createUniqueSpot();
      agent
        .put(`/spots/${validSpotId}`)
        .send(spotData)
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken)
        .expect("Content-Type", /json/)
        .end(function (err, res) {
          expect(err).to.not.exist;
          done();
        });
    });

    it("Authentication", function (done) {
      const spotData = createUniqueSpot();
      let validSpotId = agentSpot.id;
      agentNonAuth
        .put(`/spots/${validSpotId}`)
        .send(spotData)
        .set("X-XSRF-TOKEN", xsrfToken3)
        .set("Accept", "application/json")
        .expect(401)
        .end(function (err, res) {
          if (err) return done(err);
          done();
        });
    });

    it("Authorization", function (done) {
      const spotData = createUniqueSpot();
      let validSpotId = agentSpot.id;
      agent2
        .put(`/spots/${validSpotId}`)
        .send(spotData)
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken2)
        .expect(403)
        .end(function (err, res) {
          if (err) return done(err);
          done();
        });
    });
  });

  describe("Response", function () {
    it("Status Code - 200", function (done) {
      let validSpotId = agentSpot.id;
      const spotData = createUniqueSpot();
      agent
        .put(`/spots/${validSpotId}`)
        .send(spotData)
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken)
        .expect("Content-Type", /json/)
        .expect(200)
        .end(function (err, res) {
          done();
        });
    });

    it("Body Matches Api Docs", function (done) {
      let validSpotId = agentSpot.id;
      const spotData = createUniqueSpot();
      agent
        .put(`/spots/${validSpotId}`)
        .send(spotData)
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken)
        .expect("Content-Type", /json/)
        .expect(200)
        .end(function (err, res) {
          expect(err).to.not.exist;
          expect(res.body).to.include.keys(expectedNeOrEditSpotKeys);
          expect(res.body.name).to.equal(spotData.name);
          expect(res.body.address).to.equal(spotData.address);
          done();
        });
    });
  });

  describe("Error Response: Body validation error", function () {
    it("Status Code - 400", function (done) {
      const incompleteData = {
        city: "San Francisco",
      };
      let validSpotId = agentSpot.id;
      agent
        .put(`/spots/${validSpotId}`)
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken)
        .send(incompleteData)
        .expect("Content-Type", /json/)
        .expect(400)
        .end(function (err, res) {
          expect(err).to.not.exist;
          done();
        });
    });
    it("Body Matches API Docs", function (done) {
      const incompleteData = {
        city: "San Francisco",
      };
      let validSpotId = agentSpot.id;
      agent
        .put(`/spots/${validSpotId}`)
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken)
        .send(incompleteData)
        .expect("Content-Type", /json/)
        .expect(400)
        .end(function (err, res) {
          expect(err).to.not.exist;
          expect(res.body).to.have.property("message");
          expect(res.body.errors).to.include.keys(
            "address",
            "lat",
            "lng",
            "name",
            "description",
            "price",
            "country",
            "state"
          );
          done();
        });
    });
  });

  describe("Error response: Couldn't find a Spot with the specified id", function () {
    it("Status Code - 404", function (done) {
      const invalidSpotId = 923058;
      const spotData = createUniqueSpot();
      agent
        .put(`/spots/${invalidSpotId}`)
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken)
        .send(spotData)
        .expect("Content-Type", /json/)
        .expect(404)
        .end(function (err, res) {
          expect(err).to.not.exist;
          done();
        });
    });

    it("Body Matches API Docs", function (done) {
      const invalidSpotId = 923058;
      const spotData = createUniqueSpot();
      agent
        .put(`/spots/${invalidSpotId}`)
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken)
        .send(spotData)
        .expect("Content-Type", /json/)
        .end(function (err, res) {
          expect(err).to.not.exist;
          expect(res.body).to.have.property(
            "message",
            "Spot couldn't be found"
          );
          done();
        });
    });
  });
});
