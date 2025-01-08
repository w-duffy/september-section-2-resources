## The Full Stack Data Flow

It is time to talk about the data flow. How everything in a full stack application works together. This is the bread and butter of your debugging. The is is the way your workflow should typically work when building a project from scratch. This is your source of truth. Memorizing this will help you master Mod 4 and 5, and will set you up to succeed with flying colors in Mod 6, capstone, and beyond. This is the exact same data flow Instructors use when we need to debug your projects.

The Data Flow is as follows:

1. **User Interface:** The user interacts with a React component (clicks a button, submits a form, etc.).
2. **Component:** The component's event handler (`handleSubmit`) dispatches a **thunk action creator** (a function that returns a thunk).
3. **Thunk:**  The thunk makes an async request (`fetch`) to the backend API route.
4. **Backend (API):** The backend API route handler validates the request, potentially interacts with the database, and will send a response.
5. **Database (Optional):** If needed, the database performs the requested operation (CRUD).
6. **Backend (API):** Sends a `json` response back to the thunk.
7. **Thunk:** Handles the response (success or error) and dispatches a regular **action** to the reducer.
8. **Action:** A POJO with a `type` property (describing the action) and an optional `payload` (data for the store).
9. **Reducer:** Receives the action, and based on the `action.type`, **immutably** updates the Redux store's state.
10. **Component:** Components connected to the store via `useSelector` are notified of state changes and re-render if necessary `if (newState.someSlice !== oldState.someSlice) render()`.
11. **User Interface:** The user sees the updated UI with the new state.

We can condense some of these to create the 9 step plan

1. Browser(user interface)
2. React component
3. Thunk
4. Backend route
5. Thunk (again)
6. Action creator
7. Reducer
8. React component (via useSelector)
9. Browser (with state now changed)
