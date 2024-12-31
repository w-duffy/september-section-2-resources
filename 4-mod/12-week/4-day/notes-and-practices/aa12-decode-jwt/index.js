// Parsing a JWT
let thing = require('crypto').randomBytes(64).toString('hex')
console.log(thing)
const sampleJwt = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Im15c2VsZkBhcHBhY2FkZW15LmlvIn0.EqRikwoGyAlfvblF_FdbnQlbAQGvWZlccFnmHOVdaLg";

// #1: Splitting the JWT into 3 parts: header, payload, signature


const jwtArray = sampleJwt.split(".");
const [ header, payload, signature ] = jwtArray;

console.log("\nHEADER: ", header);
console.log("\nPAYLOAD: ", payload);
console.log("\nSIGNATURE: ", signature);


// #2: Decoding a JWT's header and payload
// Hint: Buffer.from(string, 'base64').toString();

const decodedHeader = Buffer.from(header, 'base64').toString();
console.log("\nDECODED HEADER: ", decodedHeader);

const decodedPayload = Buffer.from(payload, 'base64').toString();
console.log("\nDECODED PAYLOAD: ", decodedPayload);
