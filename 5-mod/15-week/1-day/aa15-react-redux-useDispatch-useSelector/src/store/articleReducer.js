import articles from '../data/data.json';

const LOAD_ARTICLES = 'article/loadArticles';
const LOAD_ONE = 'article/loadOne';

export const loadArticles = () => {
  return {
    type: LOAD_ARTICLES,
    articles
  };
};

const initialState = { entries: [], isLoading: true, byId: {} };
// const initialState = [];

const articleReducer = (state = initialState, action) => {
  switch (action.type) {
    case LOAD_ARTICLES:
      return { ...state, entries: [...action.articles] };
      case LOAD_ONE:
        return { ...state, byId: action.payload };  
    default:
      return state;
  }
};

export default articleReducer;
