import { expect } from "chai";
import { apiBaseUrl } from "../utils/constants.mjs";
import {
  createAgent,
  agentCreateSpot,
  fetchCsrfToken,
  agentSignUp,
  agentCreateReview,
  createManyAgents,
  fetchManyCsrfTokens,
} from "../utils/agent-factory.mjs";

describe("\nGet all Reviews of the Current User", function () {
  let agent,
    xsrfToken,
    agent2,
    xsrfToken2,
    agentSpot,
    agent2Spot,
    agentReview,
    agent3,
    xsrfToken3;

  before(async function () {
    this.timeout(15000);
    [agent, agent2, agent3] = createManyAgents(apiBaseUrl, 3);
    [xsrfToken, xsrfToken2, xsrfToken3] = await fetchManyCsrfTokens([agent, agent2, agent3]);

    await agentSignUp(agent, xsrfToken);
    let res = await agentCreateSpot(agent, xsrfToken);
    agentSpot = res.body;

    await agentSignUp(agent2, xsrfToken2);
    let agent2Res = await agentCreateSpot(agent2, xsrfToken2);
    agent2Spot = agent2Res.body;

    let reviewRes = await agentCreateReview(agent, xsrfToken, agent2Spot.id);
    agentReview = reviewRes.body;
  });

  describe("GET /api/reviews/current", function () {
    it("Correct Endpoint", function (done) {
      agent.get("/reviews/current").end(function (err, res) {
        expect(err).to.not.exist;
        done();
      });
    })

    it("Authentication", function (done) {
      agent3
        .get("/reviews/current")
        .set("X-XSRF-TOKEN", xsrfToken3)
        .expect(401)
        .end(function (err, res) {
          if (err) return done(err);
          done();
        });
    })
  });

  describe("Response", function () {
    it("Status Code - 200", function (done) {
      agent
        .get("/reviews/current")
        .expect(200)
        .end(function (err, res) {
          expect(err).to.not.exist;
          done();
        });
    });

    it("Body Matches API Docs", function (done) {
      agent
        .get("/reviews/current")
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken)
        .expect("Content-Type", /json/)
        .expect(200)
        .end(function (err, res) {
          expect(err).to.not.exist;
          expect(res.body).to.be.an("object");
          expect(res.body).to.have.property("Reviews").that.is.an("array");


          if (res.body.Reviews.length > 0) {
            const review = res.body.Reviews[0];
            expect(review).to.include.keys(
              "id",
              "userId",
              "spotId",
              "review",
              "stars",
              "createdAt",
              "updatedAt",
              "User",
              "Spot",
              "ReviewImages"
            );
            expect(review.User).to.include.keys("id", "firstName", "lastName");
            expect(review.Spot).to.include.keys(
              "id",
              "ownerId",
              "address",
              "city",
              "state",
              "country",
              "lat",
              "lng",
              "name",
              "price",
              "previewImage"
            );
            expect(review.ReviewImages).to.be.an("array");
          }
          done();
        });
    });
  });
});
