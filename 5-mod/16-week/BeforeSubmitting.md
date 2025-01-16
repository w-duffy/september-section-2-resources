# Testing Your App Before Submission

After you've completed the scorecard and checked every box, perform a comprehensive end-to-end test of your application before submitting it for grading.

The following is a summary of the minimum end-to-end testing you should perform.

## 1. Validate All Inputs

Thoroughly search your codebase to find **every** input field. Ensure each input has appropriate validations to prevent invalid data from being submitted. Examples include:

*   **Price:** Should be a numerical value greater than 0.00.
*   **String Length:** Implement reasonable maximum and minimum length validations for text fields.
*   **Required Fields:** Prevent submission of required fields with blank or null values.

See the [Client Side Form Validation Cheat Sheet](CheckingInputs.md) for more details.

## 2. End-to-End Testing as a New User

Perform a complete test of each feature from the perspective of a **newly** signed-up user. Follow these steps:

*   Sign up as a new user.
*   Log out.
*   Log back in as that user.
*   Create two spots.
*   Update the first spot.
*   Log out.

## 3. Testing with a Second User

Sign in as a different, newly created user and perform the following actions:

*   Write a review on one of the spots created in Step 2.
*   Delete the review.
*   Write another review on the same spot.
*   Log out.

## 4. Testing as the Original User

Log back in as the user created in Step 2 and follow the steps below to ensure your associations are correct:

*   Update one of the spots created in Step 2.
*   Delete one of the spots created in Step 2.

## 5. Testing for Edge Cases

Beyond the normal "happy path" user experience (UX), where a user interacts correctly with your app, test for the following edge cases:

*   **Hard Refresh:** On every page, as both a logged-in and a logged-out user, perform a hard refresh to ensure the app doesn't crash or behave unexpectedly.
*   **Invalid Inputs:** Attempt to submit forms with invalid inputs, testing every input field in your application.
*   **Logout/Login on Every Page:** Try logging out and logging back in on every page of your app, ensuring that the app doesn't crash.
