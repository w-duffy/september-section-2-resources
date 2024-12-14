import { expect } from "chai";
import { apiBaseUrl } from "../utils/constants.mjs";
import { expectedSpotKeys } from "../utils/err-helpers.mjs";
import {
  agentCreateSpot,
  agentSignUp,
  createManyAgents,
  fetchManyCsrfTokens,
} from "../utils/agent-factory.mjs";

describe("Add Query Filters to Get All Spots", function () {
  let agent, xsrfToken, agentSpot, agent2, xsrfToken2;

  before(async function () {
    this.timeout(15000);
    [agent, agent2] = createManyAgents(apiBaseUrl, 2);
    [xsrfToken, xsrfToken2] = await fetchManyCsrfTokens([agent, agent2]);
    await agentSignUp(agent, xsrfToken);
    let res = await agentCreateSpot(agent, xsrfToken);
    agentSpot = res.body;
  });

  describe("GET /api/spot?query=params", function () {
    it("Correct Endpoint", function (done) {
      agent
        .get("/spots")
        .query({})
        .expect("Content-Type", /json/)
        .end(function (err, res) {
          expect(err).to.not.exist;
          done();
        });
    });
  });

  describe("Response", function () {
    it("Status Code - 200", function (done) {
      agent
        .get("/spots")
        .query({})
        .expect("Content-Type", /json/)
        .expect(200)
        .end(function (err, res) {
          expect(err).to.not.exist;
          done();
        });
    });

    describe("Body Matches API Docs", function () {
      it("No filter", function (done) {
        agent
          .get("/spots")
          .query({})
          .expect("Content-Type", /json/)
          .end(function (err, res) {
            expect(err).to.not.exist;
            expect(res.body).to.be.an("object");
            expect(res.body).to.have.property("Spots").that.is.an("array");
            expect(res.body).to.include.keys("page", "size");
            expect(res.body.page).to.equal(1);
            expect(res.body.size).to.equal(20);
            if (res.body.Spots.length > 0) {
              const spot = res.body.Spots[0];
              expect(spot).to.include.keys(expectedSpotKeys);
            }
            done();
          });
      });

      it("returns spots filtered by lat/lng", function (done) {
        agent
          .get("/spots")
          .query({
            minLat: 35,
            maxLat: 40,
            minLng: -123,
            maxLng: -120,
          })
          .expect("Content-Type", /json/)
          .expect(200)
          .end(function (err, res) {
            expect(err).to.not.exist;
            expect(res.body).to.have.property("Spots").that.is.an("array");
            done();
          });
      });

      it("returns spots filtered by price range", function (done) {
        agent
          .get("/spots")
          .query({
            minPrice: 100,
            maxPrice: 200,
          })
          .expect("Content-Type", /json/)
          .expect(200)
          .end(function (err, res) {
            expect(err).to.not.exist;
            expect(res.body).to.have.property("Spots").that.is.an("array");
            done();
          });
      });
    });
  });

  describe("Error Response: Query parameter validation errors", function () {
    describe("Status Code - 400", function () {
      it("returns an error for invalid query parameters", function (done) {
        agent
          .get("/spots")
          .query({
            size: "niceTest!",
            page: "testing",
          })
          .expect("Content-Type", /json/)
          .expect(400)
          .end(function (err, res) {
            expect(err).to.not.exist;
            done();
          });
      });

      it("returns an error for invalid min/max lng", function (done) {
        agent
          .get("/spots")
          .query({
            minLat: "potato",
            minLng: "ceremony",
          })
          .expect("Content-Type", /json/)
          .expect(400)
          .end(function (err, res) {
            done();
          });
      });
    });

    describe("Body Matches API Docs", function () {
      it("returns an error for invalid query parameters", function (done) {
        agent
          .get("/spots")
          .query({
            size: "niceTest!",
            page: "testing",
          })
          .expect("Content-Type", /json/)
          .end(function (err, res) {
            expect(err).to.not.exist;
            expect(res.body).to.have.property("message");
            expect(res.body.errors).to.include.keys("page", "size");
            done();
          });
      });

      it("returns an error for invalid min/max lng", function (done) {
        agent
          .get("/spots")
          .query({
            minLat: "potato",
            minLng: "ceremony",
          })
          .expect("Content-Type", /json/)
          .end(function (err, res) {
            expect(err).to.not.exist;
            expect(res.body).to.have.property("message");
            expect(res.body.errors).to.include.keys("minLat", "minLng");
            done();
          });
      });
    });
  });
});
