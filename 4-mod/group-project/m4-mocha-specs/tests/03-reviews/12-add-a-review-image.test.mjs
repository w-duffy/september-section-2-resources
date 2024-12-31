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
import { generateUniqueUsername } from "../utils/agent-helpers.mjs";

describe("\nAdd an Image to a Review based on the Review's id", function () {
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

  describe("POST /api/reviews/:reviewId/images", function () {
    it("Correct Endpoint", function (done) {
      const imageData = {
        url: "imageTest.png",
      };
      agent2
        .post(`/reviews/${agent2Review.id}/images`)
        .send(imageData)
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken2)
        .expect("Content-Type", /json/)
        .end(function (err, res) {
          expect(err).to.not.exist;
          done();
        });
    });

    it("Authentication", function (done) {
      const imageData = {
        url: `${generateUniqueUsername()}.png`,
      };
      agent4
        .post(`/reviews/${agent2Review.id}/images`)
        .send(imageData)
        .set("X-XSRF-TOKEN", xsrfToken4)
        .set("Accept", "application/json")
        .expect(401)
        .end(function (err, res) {
          if (err) return done(err);
          done();
        });
    })

    it("Authorization", function (done) {
      const imageData = {
        url: `${generateUniqueUsername()}.png`,
      };
      agent3
        .post(`/reviews/${agent2Review.id}/images`)
        .set("X-XSRF-TOKEN", xsrfToken3)
        .set("Accept", "application/json")
        .send(imageData)
        .expect(403)
        .end(function (err, res) {
          if (err) return done(err);
          done();
        });
    })

  });


  describe("Response", function () {
    it("Status Code - 201", function (done) {
      const imageData = {
        url: `${generateUniqueUsername()}.png`,
      };
      agent2
        .post(`/reviews/${agent2Review.id}/images`)
        .send(imageData)
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken2)
        .expect(201)
        .end(function (err, res) {
          if (err) return done(err);
          done();
        });
    })

    it("Body Matches API Docs", function (done) {
      const imageData = {
        url: `${generateUniqueUsername()}.png`,
      };
      agent2
        .post(`/reviews/${agent2Review.id}/images`)
        .send(imageData)
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken2)
        .end(function (err, res) {
          expect(err).to.not.exist;
          expect(res.body).to.be.an("object");
          expect(res.body).to.include.keys("id", "url");
          expect(res.body.url).to.equal(imageData.url);
          done();
        });
    })
  });

  describe("Error response: Couldn't find a Review with the specified id", function () {
    it("Status Code - 404", function (done) {
      const imageData = {
        url: `${generateUniqueUsername()}.png`,
      };
      agent2
        .post(`/reviews/2523532/images`)
        .send(imageData)
        .set("Accept", "application/json")
        .set("X-XSRF-TOKEN", xsrfToken2)
        .expect("Content-Type", /json/)
        .expect(404)
        .end(function (err, res) {
          if (err) return done(err);
          done();
        });
    });

    it("Body Matches API Docs", function (done) {
      const imageData = {
        url: `${generateUniqueUsername()}.png`,
      };

      agent2
        .post(`/reviews/2523532/images`)
        .send(imageData)
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
