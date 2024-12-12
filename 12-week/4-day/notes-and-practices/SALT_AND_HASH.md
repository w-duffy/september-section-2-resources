# Salting

An extra security measure we can take to protect passwords
- Adds a random value to a password before hashing (we can use bycrpt for hashing)
- Prevents a malicious user from figuring out 1 password and knowing other passwords that match the same hash
- Prevents Rainbow attacks (brute forcing)

## Implementation
- Generate a salt
- Combine user's password and salt and run it through a hashing algorithm.
- Save the salted and hashed password to the DB.
