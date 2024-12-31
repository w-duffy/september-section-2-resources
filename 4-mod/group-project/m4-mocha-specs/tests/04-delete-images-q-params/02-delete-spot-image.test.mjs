import { expect } from "chai";
import { apiBaseUrl } from "../utils/constants.mjs";
import {
  createAgent,
  agentSignUp,
  fetchCsrfToken,
  agentCreateSpot,
  agentCreateSpotImage
} from "../utils/agent-factory.mjs";

describe("\nDelete a Spot Image", function () {
  let agent, xsrfToken, spot, spotImage, spotImage1, xsrfToken2, agent2, spot2, spotImage2, agent3, xsrfToken3;

  before(async function () {
    this.timeout(15000);
    agent = createAgent(apiBaseUrl);

    xsrfToken = await fetchCsrfToken(agent);
    await agentSignUp(agent, xsrfToken);

    let spotRes = await agentCreateSpot(agent, xsrfToken);
    spot = spotRes.body;

    let imageRes = await agentCreateSpotImage(agent, xsrfToken, spot.id);
    spotImage = imageRes.body;

    let imageRes1 = await agentCreateSpotImage(agent, xsrfToken, spot.id);
    spotImage1 = imageRes1.body;

    //! Agent 2

    agent2 = createAgent(apiBaseUrl);
    xsrfToken2 = await fetchCsrfToken(agent2);
    await agentSignUp(agent2, xsrfToken2);

    let spotRes2 = await agentCreateSpot(agent2, xsrfToken2);
    spot2 = spotRes2.body;

    let imageRes2 = await agentCreateSpotImage(agent2, xsrfToken2, spot2.id);
    spotImage2 = imageRes2.body;

    agent3 = createAgent(apiBaseUrl);
    xsrfToken3 = await fetchCsrfToken(agent3);
  });

  describe("DELETE /api/spot-images/:imageId", function () {
    it("Correct Endpoint", function (done) {
      agent
        .delete(`/spot-images/${spotImage.id}`)
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken)
        .expect("Content-Type", /json/)
        .end(function (err, res) {
          expect(err).to.not.exist;
          done();
        });
    }); 

    it("Authentication", function (done) {
      agent3
        .delete(`/spot-images/${spotImage.id}`)
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken3)
        .expect("Content-Type", /json/)
        .expect(401)
        .end(function (err, res) {
          if (err) return done(err);
          return done();

        });
    });

    it("Authorization", function (done) {
      agent
        .delete(`/spot-images/${spotImage2.id}`)
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken)
        .expect("Content-Type", /json/)
        .expect(403)
        .end(function (err, res) {
          if (err) return done(err);
          return done();
        });
    }); 
  }); 

  describe("Response", function () {
    it("Status Code - 200", function (done) {
      agent
        .delete(`/spot-images/${spotImage.id}`)
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken)
        .expect("Content-Type", /json/)
        .expect(200)
        .end(function (err, res) {
          done();
        });
    }); 

    it("Body Matches API Docs", function (done) {
      agent
        .delete(`/spot-images/${spotImage1.id}`)
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

  describe("Error response: Couldn't find a Spot Image with the specified id", function () {
    it("Status Code - 404", function (done) {
      agent
        .delete(`/spot-images/2352352`)
        .expect("Content-Type", /json/)
        .set("X-XSRF-TOKEN", xsrfToken)
        .expect(404)
        .end(function (err, res) {
          if(err) return done(err);
          done();
        });
    }); 
    it("Body Matches API Docs", function (done) {
      agent
        .delete(`/spot-images/2352352`)
        .expect("Content-Type", /json/)
        .set("X-XSRF-TOKEN", xsrfToken)
        .end(function (err, res) {
          expect(err).to.not.exist;
          expect(res.body).to.have.property("message", "Spot Image couldn't be found");
          done();
        });
    });
  })
})
