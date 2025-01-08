import { applyMiddleware, combineReducers, compose, createStore } from 'redux';
import reportsReducer from './reportsReducer';

const rootReducer = combineReducers({
    reports: reportsReducer,
});

let enhancer;

if (import.meta.env.MODE === 'development') {
    const logger = (await import('redux-logger')).default;
    const composeEnhancers =
        typeof window === 'object' &&
        window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__
            ? window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__({ trace: true })
            : compose;
    enhancer = composeEnhancers(applyMiddleware(logger));
}

export const configureStore = (preloadedState) => {
    return createStore(rootReducer, preloadedState, enhancer);
};

export default configureStore;
