import articles from '../data/data.json';

const LOAD_ARTICLES = 'article/loadArticles';
const ADD_ARTICLE = 'article/addArticle'; //? 'pleaseReduxAddAnArticle' <- okay! but just kinda weird
const REMOVE_ALL_ARTICLES = 'article/removeAllArticles';

export const loadArticles = () => {
    return {
        type: LOAD_ARTICLES,
        articles,
    };
};

export const addArticle = (payload) => {
    return {
        type: ADD_ARTICLE,
        payload,
    };
};

export const articleKilla = () => {
    return {
        type: REMOVE_ALL_ARTICLES,
    };
};

const initialState = { entries: [], isLoading: true};

const articleReducer = (state = initialState, action) => {
    // console.log("HEY LOOK I'M THE ARTICLE REDUCER");
    let newState
    switch (action.type) {
        case LOAD_ARTICLES:
            return { ...state, entries: [...action.articles] };
        case ADD_ARTICLE:
            // DO NOT DO THIS ~~~~~~~~~~~~~~~~~~~
            newState = {...state} 
            newState.entries.push(action.payload) // mutating state == don't do this
            return newState
            // DO NOT DO THIS ~~~~~~~~~~~~~~~~~~~
            
            // Good! Immutable update
            // return { ...state, entries: [...state.entries, action.payload] };
        //  return { ...state, entries: [action.payload] };
        case REMOVE_ALL_ARTICLES:
            return { entries: [], isLoading: true };
        default:
            return state;
    }
};

export default articleReducer;
