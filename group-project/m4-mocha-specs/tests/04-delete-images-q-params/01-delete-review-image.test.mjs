import { expect } from "chai";
import { apiBaseUrl } from "../utils/constants.mjs";
import {
  agentSignUp,
  agentCreateSpot,
  agentCreateReview,
  agentCreateReviewImage,
  createManyAgents,
  fetchManyCsrfTokens,
  createAgent,
  fetchCsrfToken
} from "../utils/agent-factory.mjs";

describe("\nDelete a Review Image", function () {
  let agent,
    xsrfToken,
    agentSpot,
    agent2,
    xsrfToken2,
    agent3,
    xsrfToken3,
    agent2Review,
    reviewImage,
    agent3Review3,
    reviewImage3,
    agent4,
    xsrfToken4;

  before(async function () {
    this.timeout(10000);
    let agentArr = createManyAgents(apiBaseUrl, 3);
    [agent, agent2, agent3] = agentArr;


    let xsrfTokens = await fetchManyCsrfTokens(agentArr);
    [xsrfToken, xsrfToken2, xsrfToken3] = xsrfTokens



    await Promise.all(agentArr.map((el, idx) => agentSignUp(el, xsrfTokens[idx])));

    let spotRes = await agentCreateSpot(agent, xsrfToken);
    agentSpot = spotRes.body;

    //! review 1
    let reviewRes = await agentCreateReview(agent2, xsrfToken2, agentSpot.id);
    agent2Review = reviewRes.body;
    let reviewImageRes = await agentCreateReviewImage(
      agent2,
      xsrfToken2,
      agent2Review.id
    );

    reviewImage = reviewImageRes.body;

    //! review 2
    let reviewRes3 = await agentCreateReview(agent3, xsrfToken3, agentSpot.id);
    agent3Review3 = reviewRes3.body;
    let reviewImageRes3 = await agentCreateReviewImage(
      agent3,
      xsrfToken3,
      agent3Review3.id
    );
    reviewImage3 = reviewImageRes3.body;

    agent4 = createAgent(apiBaseUrl);
    xsrfToken4 = await fetchCsrfToken(agent4);
  });

  describe("DELETE /api/review-images/:imageId", function () {
    it("Correct Endpoint", function (done) {
      agent2
        .delete(`/review-images/${reviewImage.id}`)
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken2)
        .expect("Content-Type", /json/)
        .end(function (err, res) {
          done();
        });
    });


    it("Authentication", function (done) {
      agent4
        .delete(`/review-images/${reviewImage.id}`)
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken4)
        .expect(401)
        .end(function (err, res) {
          if (err) return done(err);
          done();
        });
    });


    it("Authorization", function (done) {
      agent2
        .delete(`/review-images/${reviewImage3.id}`)
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken2)
        .expect(403)
        .end(function (err, res) {
          if (err) return done(err);
          done();
        });
    });
  })

  describe("Response", function () {
    it("Status Code - 200", function (done) {
      agent2
        .delete(`/review-images/${reviewImage.id}`)
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken2)
        .expect("Content-Type", /json/)
        .expect(200)
        .end(function (err, res) {
          done();
        });
    });


    it("Body Matches API Docs", function (done) {
      agent3
        .delete(`/review-images/${reviewImage3.id}`)
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken3)
        .expect("Content-Type", /json/)
        .end(function (err, res) {
          expect(err).to.not.exist;
          expect(res.body).to.have.property("message", "Successfully deleted");
          done();
        });
    });
  })

  describe("Error response: Couldn't find a Review Image with the specified id", function () {
    it("Status Code - 404", function (done) {
      agent2
        .delete(`/review-images/252352352`)
        .set("X-XSRF-TOKEN", xsrfToken2)
        .expect("Content-Type", /json/)
        .expect(404)
        .end(function (err, res) {
          if (err) return done(err);
          done();
        });
    });

    it("Body Matches API Docs", function (done) {
      agent2
        .delete(`/review-images/252352352`)
        .set("X-XSRF-TOKEN", xsrfToken2)
        .expect("Content-Type", /json/)
        .end(function (err, res) {
          expect(err).to.not.exist;
          expect(res.body).to.have.property(
            "message",
            "Review Image couldn't be found"
          );
          done();
        });
    });
  })


});
