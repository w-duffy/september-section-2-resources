import { assert, expect } from "chai";
import { apiBaseUrl } from "../utils/constants.mjs";
import { createAgent } from "../utils/agent-factory.mjs";

describe("Get all Spots", function () {
  let agent;
  before(async function () {
    this.timeout(15000);
    agent = createAgent(apiBaseUrl);
  });

  describe("GET /api/spots", function () {
    it("Correct Endpoint", function (done) {
      agent.get("/spots").end(function (err, res) {
        expect(err).to.not.exist;
        done();
      });
    });
  });
  describe("Response", function () {
    it("Status Code - 200", function (done) {
      agent
        .get("/spots")
        .expect(200)
        .end(function (err, res) {
          expect(err).to.not.exist;
          done();
        });
    });
    it("Body Matches API Docs", function (done) {
      let errors = [];
      agent
        .get("/spots")
        .set("Accept", "application/json")
        .expect(200)
        .expect("Content-Type", /json/)

        .end(function (err, res) {
          if (err) errors.push("Error in second request: " + err.message);
          try {
            const spots = res.body.Spots;

            assert(Array.isArray(spots), "Spots should be an array");
            assert(spots.length > 0, "Spots array should not be empty");
            const spot = spots[0];
            assert.strictEqual(typeof spot.id, "number", "id should be a number");
            assert.strictEqual(typeof spot.ownerId, "number", "ownerId should be a number");
            assert.strictEqual(typeof spot.address, "string", "address should be a string");
            assert.strictEqual(typeof spot.city, "string", "city should be a string");
            assert.strictEqual(typeof spot.state, "string", "state should be a string");
            assert.strictEqual(typeof spot.country, "string", "country should be a string");
            assert.strictEqual(typeof spot.lat, "number", "lat should be a number");
            assert.strictEqual(typeof spot.lng, "number", "lng should be a number");
            assert.strictEqual(typeof spot.name, "string", "name should be a string");
            assert.strictEqual(typeof spot.description, "string", "description should be a string");
            assert.strictEqual(typeof spot.price, "number", "price should be a number");
            assert.strictEqual(typeof spot.createdAt, "string", "createdAt should be a string");
            assert.strictEqual(typeof spot.updatedAt, "string", "updatedAt should be a string");
            expect(spot).to.have.property("avgRating");
            expect(spot).to.have.property("previewImage");
          } catch (err) {
            errors.push("Assertion error: " + err.message);
          }

          if (errors.length > 0) {
            done(new Error(errors.join("\n")));
          } else {
            done();
          }
        });
    });
  });
});
