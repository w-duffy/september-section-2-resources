import { expect } from "chai";
import { apiBaseUrl } from "../utils/constants.mjs";
import {
  agentSignUp,
  agentCreateSpot,
  agentCreateReview,
  createManyAgents,
  fetchManyCsrfTokens,
} from "../utils/agent-factory.mjs";

describe("\nGet all Reviews by a Spot's id", function () {
  let agent, xsrfToken, agentSpot, agent2, xsrfToken2, agent3, xsrfToken3;

  before(async function () {
    this.timeout(15000);
    let agentArr = createManyAgents(apiBaseUrl, 3);
    [agent, agent2, agent3] = agentArr;
    let xsrfTokens = await fetchManyCsrfTokens(agentArr);
    [xsrfToken, xsrfToken2, xsrfToken3] = xsrfTokens;
    await Promise.all(agentArr.map((el, idx) => agentSignUp(el, xsrfTokens[idx])));

    let spotRes = await agentCreateSpot(agent, xsrfToken);
    agentSpot = spotRes.body;
    await agentCreateReview(agent2, xsrfToken2, agentSpot.id);
    await agentCreateReview(agent3, xsrfToken3, agentSpot.id);
  });


  describe("GET /api/spots/:spotId/reviews", function () {
    it("Correct Endpoint", function (done) {
      agent
        .get(`/spots/${agentSpot.id}/reviews`)
        .end(function (err, res) {
          expect(err).to.not.exist;
          done();
        })
      });
  });

  describe("Response", function () {
    it("Status Code - 200", function (done) {
      agent
        .get(`/spots/${agentSpot.id}/reviews`)
        .expect(200)
        .end(function (err, res) {
          expect(err).to.not.exist;
          done();
        })
      }); 

      it("Body Matches API Docs", function (done) {
        agent
          .get(`/spots/${agentSpot.id}/reviews`)
          .set("Accept", "application/json")
          .set("X-XSRF-TOKEN", xsrfToken)
          .expect("Content-Type", /json/)
          .end(function (err, res) {
            expect(err).to.not.exist;
            expect(res.body).to.be.an("object");
            expect(res.body).to.have.property("Reviews").that.is.an("array");

            if (res.body.Reviews.length > 0) {
              const reviewDetails = res.body.Reviews[0];
              expect(reviewDetails).to.include.keys(
                "id",
                "userId",
                "spotId",
                "review",
                "stars",
                "createdAt",
                "updatedAt",
                "User",
                "ReviewImages"
              );
              expect(reviewDetails.User).to.include.keys(
                "id",
                "firstName",
                "lastName"
              );
              expect(reviewDetails.ReviewImages).to.be.an("array");
            }
            done();
          });
      }); 

  }); 

  describe("Error response: Couldn't find a Spot with the specified id", function () {

    it("Status Code - 404", function (done) {
      agent
        .get(`/spots/820329/reviews`)
        .expect("Content-Type", /json/)
        .expect(404)
        .end(function (err, res) {
          expect(err).to.not.exist;
          done();
        });
    }); 

    it("Body Matches API Docs", function (done) {
      agent
        .get(`/spots/820329/reviews`)
        .expect("Content-Type", /json/)
        .end(function (err, res) {
          expect(err).to.not.exist;
          expect(res.body).to.have.property("message", "Spot couldn't be found");
          done();
        });
    });

  });


}); 
