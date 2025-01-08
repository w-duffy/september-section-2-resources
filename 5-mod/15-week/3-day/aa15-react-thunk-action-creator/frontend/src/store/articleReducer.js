// import articles from "../data/data.json";
import { createSelector } from "reselect";

//! --------------------------------------------------------------------
//*                            Action Types
//! --------------------------------------------------------------------
const LOAD_ARTICLES = "article/loadArticles";
const ADD_ARTICLE = "article/addArticle";

//! --------------------------------------------------------------------
//*                           Action Creators
//! --------------------------------------------------------------------

export const loadArticles = (payload) => {
  return {
    type: LOAD_ARTICLES,
    payload,
  };
};

export const addArticle = (payload) => {
  return {
    type: ADD_ARTICLE,
    payload,
  };
};

//! --------------------------------------------------------------------
//*                        Normalizing Function
//! --------------------------------------------------------------------

const normalizer = (array) => {
  const payload = {};

  array.forEach((el) => {
    payload[el.id] = el;
  });

  return payload;
};

//! --------------------------------------------------------------------
//*                             Selectors
//! --------------------------------------------------------------------

// const allArticles= useSelector((state) => state.articleState.entries);
// const articles = Object.values(allArticles);


export const articleSelector = createSelector(
  (state) => state.articleState.entries,
  (allArticles) => Object.values(allArticles)
);

//! --------------------------------------------------------------------
//?                              Thunks
//! --------------------------------------------------------------------

export const loadArticlesThunk = () => async (dispatch, getState) => {
  const res = await fetch("/api/articles");

    console.log("getState():", getState());

  if (res.ok) {
    const articles = await res.json();

    dispatch(loadArticles(normalizer(articles)));
    return null;
  } else {
    const errors = await res.json();
    return errors;
  }
};

const ERRORS = "articles/ADD_ARTICLE_ERRORS"
export const addArticleErrors = (payload) => {
  return {
    type: ERRORS,
    payload,
  };
};



export const addArticleThunk = (articleFormData) => async (dispatch) => {
  const res = await fetch("/api/articles", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(articleFormData),
  });

  // const data = await res.json() //? Write once outside the if else

  if (res.ok) {
    const newArticle = await res.json();
    dispatch(addArticle(normalizer([newArticle])));
    return {message: "success"};
  } else {
    const errors = await res.json()
    console.log("ERROR", errors.errors)
    dispatch(addArticleErrors(errors.errors))
    return errors;
  }
};

//! --------------------------------------------------------------------
//*                              Reducer
//! --------------------------------------------------------------------

// {
//     1: {
//         id: 1,
//         data: "here"
//     },
//     2: {
//         id: 2,
//         data: "here"
//     },
// }

const initialState = { entries: {}, isLoading: true, errors: [] };

// const articleReducer = (state = initialState, { type, payload }) => {
const articleReducer = (state = initialState, action) => {
  switch (action.type) {
    case LOAD_ARTICLES:
      // iterate in here over payload to add to entries
      // or handle this in the Thunk Action
    // console.log(state.entries !== newState.entries )

      return { ...state, entries: { ...action.payload } };
    case ADD_ARTICLE:
      return { ...state, entries: { ...state.entries, ...action.payload }, errors: [] };
    case ERRORS:
      console.log("in article reducer", action.payload)
      return { ...state, errors: action.payload }



    // case DELETE_ARTICLE: {
      // let newState = {...state, entries: {...state.entries}}
      // let newState = {...state}

    //   delete newState.entries[action.payload]
    //   return newState

    // }

      default:
      return state;
  }
};

export default articleReducer;

//! --------------------------------------------------------------------
//*                         Basic Catch All Thunk
//! --------------------------------------------------------------------
// export const loadArticlesThunk = () => async (dispatch, getState) => {
//   try {
//     const res = await fetch("/api/articles/hey/look/at/me");

//     if (res.ok) {
//       console.log("Things went well");
//     } else {
//       console.log("Things did not go so well :(");
//     }
//   } catch (e) {
//     console.log("This was my error", e);
//   }
// };
