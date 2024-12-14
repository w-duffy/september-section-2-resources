import { expect } from "chai";
import { apiBaseUrl } from "../utils/constants.mjs";
import {
  agentCreateSpot,
  agentSignUp,
  createManyAgents,
  fetchManyCsrfTokens,
} from "../utils/agent-factory.mjs";

describe("\nDelete a Spot", function () {
  let agent,
    xsrfToken,
    agentSpot,
    agent2,
    xsrfToken2,
    agent2Spot,
    agentSpot2,
    agentSpot3,
    agentSpot4,
    agentSpot5,
    agentSpot6,
    agentNonAuth,
    xsrfToken3;

  before(async function () {
    this.timeout(15000);
    [agent, agent2, agentNonAuth] = createManyAgents(apiBaseUrl, 3);
    [xsrfToken, xsrfToken2, xsrfToken3] = await fetchManyCsrfTokens([agent, agent2, agentNonAuth]);
    await agentSignUp(agent, xsrfToken);
    await agentSignUp(agent2, xsrfToken2);

    let res = await agentCreateSpot(agent, xsrfToken);
    let spotForDeleting1 = await agentCreateSpot(agent, xsrfToken);
    let spotForDeleting2 = await agentCreateSpot(agent, xsrfToken);
    let spotForDeleting3 = await agentCreateSpot(agent, xsrfToken);
    let spotForDeleting4 = await agentCreateSpot(agent, xsrfToken);
    let spotForDeleting5 = await agentCreateSpot(agent, xsrfToken);
    agentSpot = res.body;
    agentSpot2 = spotForDeleting1.body;
    agentSpot3 = spotForDeleting2.body;
    agentSpot4 = spotForDeleting3.body;
    agentSpot5 = spotForDeleting4.body;
    agentSpot6 = spotForDeleting5.body;

    let res2 = await agentCreateSpot(agent, xsrfToken, agentSpot.id);
    agent2Spot = res2.body;

  });

  describe("DELETE /api/spots/:spotId", function () {
    it("Correct Endpoint", function (done) {
      const spotId = agentSpot2.id;
      agent
        .delete(`/spots/${spotId}`)
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken)
        .expect("Content-Type", /json/)
        .end(function (err, res) {
          done();
        });
    });
    it("Authentication", function (done) {
      const spotId = agentSpot3.id;
      agentNonAuth
        .delete(`/spots/${spotId}`)
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken3)
        .expect(401)
        .end(function (err, res) {
          if(err) return done(err);
          done();
        });
    });
    it("Authorization", function (done) {
      const spotId = agentSpot4.id;
      agent2
        .delete(`/spots/${spotId}`)
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken2)
        .expect(403)
        .end(function (err, res) {
        if(err) return done(err);
        done();
        });
    });
  });

  describe("Response", function () {
    it("Status Code - 200", function (done) {
      const spotId = agentSpot5.id;
      agent
        .delete(`/spots/${spotId}`)
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken)
        .expect("Content-Type", /json/)
        .expect(200)
        .end(function (err, res) {
          done();
        });
    });

    it("Body Matches Api Docs", function (done) {
      const spotId = agentSpot6.id;
      agent
        .delete(`/spots/${spotId}`)
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken)
        .expect("Content-Type", /json/)
        .end(function (err, res) {
          expect(err).to.not.exist;
          expect(res.body).to.have.property("message", "Successfully deleted");
          done();
        });
    });
  });

  describe("Error Response", function () {
    it("Status Code - 404", function (done) {
      const invalidSpotId = 99325;
      agent
        .delete(`/spots/${invalidSpotId}`)
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken)
        .expect("Content-Type", /json/)
        .expect(404)
        .end(function (err, res) {
          expect(err).to.not.exist;
          done();
        });
    });

    it("Body Matches API Docs", function (done) {
      const invalidSpotId = 99325;
      agent
        .delete(`/spots/${invalidSpotId}`)
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken)
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
