import initialReports from '../data/initial-reports.json';

//! Action types
const REMOVE_REPORT = 'reports/remove';
const RECEIVE_REPORT = 'reports/receive';
const RESET_REPORTS = 'reports/reset';
// const CREATE_REPORT = 'report/create';
// const UPDATE_REPORT = 'report/update';

//? Action Creators
export const removeReport = (payload) => ({ type: REMOVE_REPORT, payload });

export const receiveReport = (payload) => ({ type: RECEIVE_REPORT, payload });

export const resetReports = () => ({ type: RESET_REPORTS });

// export const createReport = (payload) => ({ type: CREATE_REPORT, payload });

// export const updateReport = (payload) => ({ type: UPDATE_REPORT, payload });

//! Selectors
import { createSelector } from 'reselect';

const selectReports = (store) => store.reports;

export const getReports = createSelector(selectReports, (reports) =>
    Object.values(reports)
);

//* Initial state setup
const initialState = {};

initialReports.forEach((el) => {
    initialState[el.id] = el;
});

export default function reportsReducer(state = initialState, action) {
    const newState = { ...state };

    switch (action.type) {
        case REMOVE_REPORT:
            delete newState[action.payload];

            return newState;

        case RECEIVE_REPORT:
            newState[action.payload.id] = action.payload;

            return newState;

        case RESET_REPORTS:
            return initialState;

        default:
            return state;

        // case CREATE_REPORT:
        //     newState[action.payload.id] = action.payload;
        //     return newState;

        // case UPDATE_REPORT:
        //     newState[action.payload.id] = action.payload;
        //     return newState;
    }
}
