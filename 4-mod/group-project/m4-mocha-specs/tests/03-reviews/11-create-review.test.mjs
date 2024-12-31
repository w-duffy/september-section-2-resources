import { expect } from "chai";
import { apiBaseUrl } from "../utils/constants.mjs";
import {
  agentSignUp,
  agentCreateSpot,
  createManyAgents,
  fetchManyCsrfTokens,
  createAgent,
  fetchCsrfToken
} from "../utils/agent-factory.mjs";

describe("\nCreate a Review for a Spot based on the Spot's id", function () {
  let agent, xsrfToken, agentSpot,
    agent2, xsrfToken2,
    agent3, xsrfToken3,
    agent4, xsrfToken4,
    agent5, xsrfToken5,
    agent6, xsrfToken6,
    agent7, xsrfToken7;

  before(async function () {
    this.timeout(15000);
    let agentArr = createManyAgents(apiBaseUrl, 6);
    [agent, agent2, agent3, agent4, agent5, agent6] = agentArr;

    let xsrfTokens = await fetchManyCsrfTokens(agentArr);
    [xsrfToken, xsrfToken2, xsrfToken3, xsrfToken4, xsrfToken5, xsrfToken6] = xsrfTokens;

    await Promise.all(agentArr.map((el, idx) => agentSignUp(el, xsrfTokens[idx])));
    agent7 = createAgent(apiBaseUrl);
    xsrfToken7 = await fetchCsrfToken(agent7);

    let spotRes = await agentCreateSpot(agent, xsrfToken);
    agentSpot = spotRes.body;
  });

  describe("POST /api/spots/:spotId/reviews", function () {
    it("Correct Endpoint", function (done) {
      const reviewData = {
        review: "This was an awesome spot for testing!",
        stars: 5,
      };
      agent2
        .post(`/spots/${agentSpot.id}/reviews`)
        .send(reviewData)
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken2)
        .end(function (err, res) {
          expect(err).to.not.exist;
          done();
        });
    });

    it("Authentication", function (done) {
      const reviewData = {
        review: "This was a cool spot for testing!",
        stars: 5,
      };
      agent7
        .post(`/spots/${agentSpot.id}/reviews`)
        .send(reviewData)
        .set("X-XSRF-TOKEN", xsrfToken7)
        .set("Accept", "application/json")
        .expect(401)
        .end(function (err, res) {
          if (err) return done(err);
          done();
        });
    })

  });

  describe("Response", function () {
    it("Status Code - 201", function (done) {
      const reviewData = {
        review: "This was an amazing spot for testing!",
        stars: 5,
      };
      agent4
        .post(`/spots/${agentSpot.id}/reviews`)
        .send(reviewData)
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken4)
        .expect(201)
        .end(function (err, res) {
          expect(err).to.not.exist;
          done();
        });
    });

    it("Body Matches API Docs", function (done) {
      const reviewData = {
        review: "This was an awesome spot for testing!",
        stars: 5,
      };
      agent5
        .post(`/spots/${agentSpot.id}/reviews`)
        .send(reviewData)
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken5)
        .expect("Content-Type", /json/)
        .end(function (err, res) {
          expect(err).to.not.exist;
          expect(res.body).to.be.an("object");
          expect(res.body).to.include.keys(
            "id",
            "userId",
            "spotId",
            "review",
            "stars",
            "createdAt",
            "updatedAt"
          );
          expect(res.body.review).to.equal(reviewData.review);
          expect(res.body.stars).to.equal(reviewData.stars);
          done();
        });

    });

  });


  describe("Error Response: Body validation errors", function () {
    it("Status Code - 400", function (done) {
      const reviewData = {
        review: "",
        stars: 6,
      };

      agent3
        .post(`/spots/${agentSpot.id}/reviews`)
        .send(reviewData)
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken3)
        .expect("Content-Type", /json/)
        .expect(400)
        .end(function (err, res) {
          expect(err).to.not.exist;
          expect(res.body)
            .to.have.property("message")
          expect(res.body.errors).to.include.keys("review", "stars");
          done();
        });
    });

    it("Body Matches API Docs", function (done) {
      const reviewData = {
        review: "",
        stars: 6,
      };
      agent3
        .post(`/spots/${agentSpot.id}/reviews`)
        .send(reviewData)
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken3)
        .expect("Content-Type", /json/)
        .end(function (err, res) {
          expect(err).to.not.exist;
          expect(res.body)
            .to.have.property("message")
          expect(res.body.errors).to.include.keys("review", "stars");
          done();
        });
    });

  });



  describe("Error Response: Couldn't find a Spot with the specified id", function () {
    it("Status Code - 404", function (done) {
      agent
        .post(`/spots/235235/reviews`)
        .send({ review: "Great spot for testing reviews!", stars: 5 })
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken)
        .expect("Content-Type", /json/)
        .expect(404)
        .end(function (err, res) {
          expect(err).to.not.exist;
          expect(res.body).to.have.property("message", "Spot couldn't be found");
          done();
        });
    });

    it("Body Matches API Docs", function (done) {
      agent
        .post(`/spots/235235/reviews`)
        .send({ review: "Great spot for testing reviews!", stars: 5 })
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken)
        .expect("Content-Type", /json/)
        .end(function (err, res) {
          expect(err).to.not.exist;
          expect(res.body).to.have.property("message", "Spot couldn't be found");
          done();
        });
    });
  });


  describe("Error Response: Review from the current user already exists for the Spot", function () {

    it("Status Code - 500", function (done) {
      const reviewData = {
        review: "This was an awesome spot for testing reviews!",
        stars: 5,
      };
      agent2
        .post(`/spots/${agentSpot.id}/reviews`)
        .send(reviewData)
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken2)
        .expect("Content-Type", /json/)
        .expect(500)
        .end(function (err, res) {
          expect(err).to.not.exist;
          expect(res.body).to.have.property(
            "message",
            "User already has a review for this spot"
          );
          done();
        });
    });

    it("Body Matches API Docs", function (done) {
      const reviewData = {
        review: "This was an awesome spot for testing reviews!",
        stars: 5,
      };
      agent2
        .post(`/spots/${agentSpot.id}/reviews`)
        .send(reviewData)
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken2)
        .expect("Content-Type", /json/)
        .end(function (err, res) {
          expect(err).to.not.exist;
          expect(res.body).to.have.property(
            "message",
            "User already has a review for this spot"
          );
          done();
        });
    });

  });

})
