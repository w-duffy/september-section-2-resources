import { expect } from "chai";
import { apiBaseUrl } from "../utils/constants.mjs";
import {
  agentSignUp,
  agentCreateSpot,
  agentCreateReview,
  createManyAgents,
  fetchManyCsrfTokens,
  createAgent,
  fetchCsrfToken
} from "../utils/agent-factory.mjs";

describe("\nEdit a Review", function () {
  let agent,
    xsrfToken,
    agentSpot,
    agent2,
    xsrfToken2,
    agent3,
    xsrfToken3,
    agent2Review,
    agent4,
    xsrfToken4;

  before(async function () {
    this.timeout(15000);
    let agentArr = createManyAgents(apiBaseUrl, 3);
    [agent, agent2, agent3] = agentArr;

    let xsrfTokens = await fetchManyCsrfTokens(agentArr);
    [xsrfToken, xsrfToken2, xsrfToken3] = xsrfTokens;
    await Promise.all(agentArr.map((el, idx) => agentSignUp(el, xsrfTokens[idx])));

    agent4 = createAgent(apiBaseUrl);
    xsrfToken4 = await fetchCsrfToken(agent4);

    let spotRes = await agentCreateSpot(agent, xsrfToken);
    agentSpot = spotRes.body;

    let reviewRes = await agentCreateReview(agent2, xsrfToken2, agentSpot.id);
    agent2Review = reviewRes.body;
  });

  describe("PUT /api/reviews/:reviewId", function () {
    it("Correct Endpoint", function (done) {
      const updateData = {
        review: "This was an awesome spot for testing edit reviews!",
        stars: 5,
      };
      agent2
        .put(`/reviews/${agent2Review.id}`)
        .send(updateData)
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken2)
        .expect("Content-Type", /json/)
        .end(function (err, res) {
          expect(err).to.not.exist;
          done();
        });
    }); 

    it("Authentication", function (done) {
      const updateData = {
        review: "This was an awesome spot for testing edit reviews!",
        stars: 5,
      };
      agent4
        .put(`/reviews/${agent2Review.id}`)
        .send(updateData)
        .set("X-XSRF-TOKEN", xsrfToken4)
        .set("Accept", "application/json")
        .expect(401)

        .end(function (err, res) {
          if (err) return done(err);
          done();
        });
    });

    it("Authorization", function (done) {
      const updateData = {
        review: "This was an awesome spot for testing edit reviews!",
        stars: 5,
      };
      agent3
        .put(`/reviews/${agent2Review.id}`)
        .send(updateData)
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken3)
        .expect(403)
        .end(function (err, res) {
          if (err) return done(err);
          done();
        });
    }); 
  }); 

  describe("Response", function () {
    it("Status Code - 200", function (done) {
      const updateData = {
        review: "This was an awesome spot for testing edit reviews!",
        stars: 5,
      };
      agent2
        .put(`/reviews/${agent2Review.id}`)
        .send(updateData)
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken2)
        .expect("Content-Type", /json/)
        .expect(200)
        .end(function (err, res) {
          expect(err).to.not.exist;
          done();
        });
    }); 

    it("Body Matches API Docs", function (done) {
      const updateData = {
        review: "This was an awesome spot for testing edit reviews!",
        stars: 5,
      };
      agent2
        .put(`/reviews/${agent2Review.id}`)
        .send(updateData)
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken2)
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
          expect(res.body.review).to.equal(updateData.review);
          expect(res.body.stars).to.equal(updateData.stars);
          done();
        });
    }); 
  }); 

  describe("Error Response: Body validation errors", function () {
    it("Status Code - 400", function (done) {
      const invalidData = {
        review: "",
        stars: 6,
      };
      agent2
        .put(`/reviews/${agent2Review.id}`)
        .send(invalidData)
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken2)
        .expect("Content-Type", /json/)
        .expect(400)
        .end(function (err, res) {
          if (err) return done(err);
          done();
        });
    }); 

    it("Body Matches API Docs", function (done) {
      const invalidData = {
        review: "",
        stars: 6,
      };
      agent2
        .put(`/reviews/${agent2Review.id}`)
        .send(invalidData)
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken2)
        .expect("Content-Type", /json/)
        .end(function (err, res) {
          expect(err).to.not.exist;
          expect(res.body).to.have.property("message");
          expect(res.body.errors).to.include.keys("review", "stars");
          done();
        });
    }); 
  }); 

  describe("Error response: Couldn't find a Review with the specified id", function () {
    it("Status Code - 404", function (done) {
      const validData = {
        review: "Really nice place!",
        stars: 4,
      };
      agent2
        .put(`/reviews/2325235`)
        .send(validData)
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken2)
        .expect("Content-Type", /json/)
        .expect(404)
        .end(function (err, res) {
          if (err) return done(err);
          return done();
        });
    }); 

    it("Body Matches API Docs", function (done) {
      const validData = {
        review: "Really nice place!",
        stars: 4,
      };
      agent2
        .put(`/reviews/2325235`)
        .send(validData)
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken2)
        .expect("Content-Type", /json/)
        .end(function (err, res) {
          expect(err).to.not.exist;
          expect(res.body).to.have.property(
            "message",
            "Review couldn't be found"
          );
          done();
        });
    });
  }); 
}); 
