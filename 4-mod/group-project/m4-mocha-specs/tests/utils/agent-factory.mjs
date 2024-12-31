import pkg from "supertest";
import { expect, assert } from "chai";

import {
  createUniqueUser,
  createUniqueSpot,
  createUniqueImage,
  createUniqueReview,
} from "./agent-helpers.mjs";
import { apiBaseUrl } from "./constants.mjs";

export function createAgent(apiBaseUrl) {
  return pkg.agent(apiBaseUrl);
}

export const createManyAgents = (apiBaseUrl, num) => Array(num).fill(0).map(() => createAgent(apiBaseUrl));

export async function fetchCsrfToken(agent) {
  const res = await agent.get("/csrf/restore").expect(200);
  const cookie = res.headers["set-cookie"].find((cookie) =>
    cookie.startsWith("XSRF-TOKEN=")
  );
  return cookie ? cookie.split(";")[0].split("=")[1] : null;
}

export const fetchManyCsrfTokens = async (agents) => Promise.all(agents.map(fetchCsrfToken));

export async function agentSignUp(agent, xsrfToken) {
  let userObj = createUniqueUser();
  try {
    const response = await agent
      .post("/users")
      .send(userObj)
      .set("Accept", "application/json")
      .set("X-XSRF-TOKEN", xsrfToken)
      .expect((response) => expect(response.status).to.be.oneOf([200, 201]));
    return response;
  } catch (e) {
    assert(!e, "Could not test this route because the 'Sign Up' route failed");
  }
}

export async function agentCreateSpot(agent, xsrfToken) {
  let spotObj = createUniqueSpot();
  try {
    const response = await agent
      .post("/spots")
      .send(spotObj)
      .set("Accept", "application/json")
      .set("X-XSRF-TOKEN", xsrfToken)
      .expect((response) => expect(response.status).to.be.oneOf([200, 201]));
    return response;
  } catch (e) {
    assert(
      !e,
      "Could not test this route because the 'Create a Spot' route failed"
    );
  }
}

export async function agentCreateSpotImage(agent, xsrfToken, spotId) {
  let spotImage = createUniqueImage();
  try {
    const response = await agent
      .post(`/spots/${spotId}/images`)
      .send(spotImage)
      .set("Accept", "application/json")
      .set("X-XSRF-TOKEN", xsrfToken)
      .expect((response) => expect(response.status).to.be.oneOf([200, 201]));
    return response;
  } catch (e) {
    assert(
      !e,
      "Could not test this route because the 'Create a Spot Image' route failed"
    );
  }
}

export async function agentCreateReviewImage(agent, xsrfToken, reviewId) {
  let reviewImage = { url: "reviewImageTest.png" };
  try {
    const response = await agent
      .post(`/reviews/${reviewId}/images`)
      .send(reviewImage)
      .set("Accept", "application/json")
      .set("X-XSRF-TOKEN", xsrfToken)
      .expect((response) => expect(response.status).to.be.oneOf([200, 201]));
    return response;
  } catch (e) {
    assert(
      e,
      "Could not test this route because the 'Create a Review Image' route failed"
    );
  }
}

export async function agentCreateReview(agent, xsrfToken, nonAgentSpotId) {
  let newReview = createUniqueReview();
  try {
    const response = await agent
      .post(`/spots/${nonAgentSpotId}/reviews`)
      .send(newReview)
      .set("Accept", "application/json")
      .set("X-XSRF-TOKEN", xsrfToken)
      .expect((response) => expect(response.status).to.be.oneOf([200, 201]));
    return response;
  } catch (e) {
    console.log(e)
    assert(
      !e,
      "Could not test this route because the 'Create a Review' route failed"
    );
  }
}
