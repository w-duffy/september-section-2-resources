import { expect } from 'chai';
import { apiBaseUrl } from '../utils/constants.mjs';
import { expectedSpotByIdKeys } from '../utils/err-helpers.mjs';
import {
    createAgent,
    agentCreateSpot,
    fetchCsrfToken,
    agentSignUp,
    agentCreateSpotImage,
} from '../utils/agent-factory.mjs';

describe('\nGet details of a Spot from an id', function () {
    let agent, xsrfToken, spotId;

    before(async function () {
        this.timeout(15000);
        agent = createAgent(apiBaseUrl);
        xsrfToken = await fetchCsrfToken(agent);
        await agentSignUp(agent, xsrfToken);
        let res = await agentCreateSpot(agent, xsrfToken);
        spotId = res.body.id;
        let imageRes = await agentCreateSpotImage(agent, xsrfToken, spotId);
        agent.image = imageRes;
    });
    describe('GET /api/spots/:spotId', function () {
        it('Correct Endpoint', function (done) {
            agent.get(`/spots/${spotId}`).end(function (err, res) {
                expect(err).to.not.exist;
                done();
            });
        });
    });

    describe('Response', function () {
        it('Status Code - 200', function (done) {
            agent
                .get(`/spots/${spotId}`)
                .expect(200)
                .end(function (err, res) {
                    expect(err).to.not.exist;
                    done();
                });
        });

        it('Body Matches API Docs', function (done) {
            agent
                .get(`/spots/${spotId}`)
                .expect('Content-Type', /json/)
                .expect(200)
                .end(function (err, res) {
                    expect(err).to.not.exist;
                    expect(res.body).to.be.an('object');
                    expect(res.body).to.include.keys(expectedSpotByIdKeys);
                    const { SpotImages, Owner, id } = res.body;
                    expect(id).to.equal(spotId);
                    expect(SpotImages).to.be.an('array');
                    expect(Owner)
                        .to.be.an('object')
                        .and.to.have.all.keys('id', 'firstName', 'lastName');
                    expect(Owner.firstName).to.be.a('string');
                    expect(Owner.lastName).to.be.a('string');
                    expect(SpotImages[0]).to.have.all.keys(
                        'id',
                        'url',
                        'preview'
                    );
                    done();
                });
        });
    });

    describe('Error Response', function () {
        it('Status Code - 404', function (done) {
            const nonExistentSpotId = 2352351;
            agent
                .get(`/spots/${nonExistentSpotId}`)
                .expect('Content-Type', /json/)
                .expect(404)
                .end(function (err, res) {
                    expect(err).to.not.exist;

                    done();
                });
        });

        it('Body Matches API Docs', function (done) {
            const nonExistentSpotId = 2352351;
            agent
                .get(`/spots/${nonExistentSpotId}`)
                .expect('Content-Type', /json/)
                .end(function (err, res) {
                    expect(err).to.not.exist;
                    expect(res.body).to.have.property(
                        'message',
                        "Spot couldn't be found"
                    );
                    done();
                });
        });
    });
});
