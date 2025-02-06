// <REDUX_CODE>
import { createStore, applyMiddleware, compose, combineReducers } from 'redux';
import {thunk} from 'redux-thunk';

let createImageThunk = (image) => async (dispatch) => {
  const response = await fetch(`/api/images`, {
    method: "POST",
    body: image
  });
  if (response.ok) {
      const resBody  = await response.json();
      let imageUrl = resBody.image.image; // this is the url; not the best col name
      dispatch({type: "ADD_IMAGE", payload: imageUrl});
    }
}

let imageReducer = (state = [], action) => {
  switch(action.type) {
    case "ADD_IMAGE":
      return [...state, action.payload]
    default:
      return state
  }
}
const rootReducer = combineReducers({images: imageReducer});

let enhancer;
if (import.meta.env.MODE === 'production') {
  enhancer = applyMiddleware(thunk);
} else {
  const logger = (await import('redux-logger')).default;
  const composeEnhancers =
    window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
  enhancer = composeEnhancers(applyMiddleware(thunk, logger));
}

const configureStore = preloadedState => {
  return createStore(rootReducer, preloadedState, enhancer);
};
// </REDUX_CODE>

// <REACT_CODE>
import { useState } from 'react'
import {Provider} from 'react-redux'
import {useDispatch} from 'react-redux'

function App() {
  const dispatch = useDispatch();
  const [image, setImage] = useState(null);
  const [imageLoading, setImageLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();

    const formData = new FormData();
    formData.append("image", image);

    setImageLoading(true);
    await dispatch(createImageThunk(formData))
}
  return (
    <>
    <h1>Image Uploads Demo</h1>
    <form
        onSubmit={handleSubmit}
        encType="multipart/form-data"
        >
        <input
          type="file"
          accept="image/*"
          onChange={(e) => setImage(e.target.files[0])}
          />
        <button type="submit">Submit</button>
        {(imageLoading)&& <p>Loading...</p>}
    </form>
    <AllImages />
    </>
  )
}
import { useSelector } from 'react-redux';
function AllImages() {
let images = useSelector((state) => state.images);
console.log("Access the images anywhere!", images)
}

const ProviderWrapper = () => {
  return (
    <Provider store={configureStore()}>
      <App />
    </Provider>
  )
}
export default ProviderWrapper
// </REACT_CODE>
