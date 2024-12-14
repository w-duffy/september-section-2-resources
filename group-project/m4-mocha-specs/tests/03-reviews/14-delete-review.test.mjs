import { expect } from "chai";
import { apiBaseUrl } from "../utils/constants.mjs";
import {
  agentSignUp,
  fetchCsrfToken,
  agentCreateSpot,
  agentCreateReview,
  createManyAgents,
  fetchManyCsrfTokens,
  createAgent,
} from "../utils/agent-factory.mjs";

describe("\nDelete a Review", function () {
  let agent,
    xsrfToken,
    agentSpot,
    agent2,
    xsrfToken2,
    agent2Review,
    agent3,
    xsrfToken3,
    agent3Review,
    agent4,
    xsrfToken4,
    agent4Review,
    agent5,
    xsrfToken5,
    agent5Review,
    agent6,
    xsrfToken6,
    agent6Review,
    agent7,
    xsrfToken7;

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

    //! review 0
    let reviewRes = await agentCreateReview(agent2, xsrfToken2, agentSpot.id);
    agent2Review = reviewRes.body;

    //! review 1
    let reviewRes1 = await agentCreateReview(agent3, xsrfToken3, agentSpot.id);
    agent3Review = reviewRes1.body;

    //! review 2
    let reviewRes2 = await agentCreateReview(agent4, xsrfToken4, agentSpot.id);
    agent4Review = reviewRes2.body;

    //! review 3
    let reviewRes3 = await agentCreateReview(agent5, xsrfToken5, agentSpot.id);
    agent5Review = reviewRes3.body;

    //! review 4
    let reviewRes4 = await agentCreateReview(agent6, xsrfToken6, agentSpot.id);
    agent6Review = reviewRes4.body;
  });

  describe("DELETE /api/reviews/:reviewId", function () {
    it("Correct Endpoint", function (done) {
      agent2
        .delete(`/reviews/${agent2Review.id}`)
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken2)
        .expect("Content-Type", /json/)
        .end(function (err, res) {
          expect(err).to.not.exist;
          done();
        });
    });

    it("Authentication", function (done) {
      agent7
        .delete(`/reviews/${agent3Review.id}`)
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken7)
        .expect(401)
        .end(function (err, res) {
          if(err) return done(err);
          return done();
        });
    });

    it("Authorization", function (done) {
      agent4
        .delete(`/reviews/${agent5Review.id}`)
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken4)
        .expect(403)
        .end(function (err, res) {
          if(err) return done(err);
          return done();
        });
    });
  });

  describe("Response", function () {
    it("Status Code - 200", function (done) {
      agent5
        .delete(`/reviews/${agent5Review.id}`)
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken5)
        .expect("Content-Type", /json/)
        .expect(200)
        .end(function (err, res) {
          expect(err).to.not.exist;
          done();
        });
    });

    it("Body Matches API Docs", function (done) {
      agent6
        .delete(`/reviews/${agent6Review.id}`)
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken6)
        .expect("Content-Type", /json/)
        .end(function (err, res) {
          expect(err).to.not.exist;
          expect(res.body).to.have.property("message", "Successfully deleted");
          done();
        });
    });
  });

  describe("Error response: Couldn't find a Review with the specified id", function () {
    it("Status Code - 404", function (done) {
      agent2
        .delete(`/reviews/523523`)
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken2)
        .expect("Content-Type", /json/)
        .expect(404)
        .end(function (err, res) {
          expect(err).to.not.exist;
          done();
        });
    });

    it("Body Matches API Docs", function (done) {
      agent2
        .delete(`/reviews/523523`)
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
