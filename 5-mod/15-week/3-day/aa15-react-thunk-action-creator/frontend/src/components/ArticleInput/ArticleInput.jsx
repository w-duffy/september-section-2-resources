import { useState } from 'react';
// import { nanoid } from 'nanoid';
import { useDispatch } from 'react-redux';
// import { useNavigate } from 'react-router-dom';
import { addArticleThunk } from '../../store/articleReducer';
import { useSelector } from 'react-redux';
import './ArticleInput.css';

import { createSelector } from "reselect";

  const articleErrorSelector = state =>{
    console.log("inside error use selector ~~~~~💃")
   return state.articleState.errors
  }


const myMemoizedErrorSelector = createSelector(
  [articleErrorSelector],
  errors => errors.map(error => error.message == "hello")
)




// const articleErrorSelectorMemoized = createSelector(
//   [articleErrorSelector],
//   errors => errors
// )



// const errors = useSelector(articleErrorSelectorMemoized)


// let myFunc = (state) => state.articleState.errors

const ArticleInput = () => {
// if oldState !== newState then re-render
// const errors = useSelector(state => state.articleState.errors)

const errors = useSelector(myMemoizedErrorSelector)

// const errors = useSelector(state =>{
//   console.log("inside error use selector ~~~~~💃")
//  return state.articleState.errors
// }
// )


  // const errors = useSelector(state =>{
  //   console.log("inside error use selector ~~~~~💃")
  //  return state.articleState.errors
  // } )




 console.log("\nin article input component\n", errors)
  const [title, setTitle] = useState('');
  const [body, setBody] = useState('');
  const [imageUrl, setImageUrl] = useState('');
  // let navigate = useNavigate()

  const dispatch = useDispatch();
// console.log("im in the article input")


  const handleSubmit = async (e) => {
    e.preventDefault();
    const newArticle = {
      // id: nanoid(),
      title,
      body,
      imageUrl
    };
    console.log("in handle submit", newArticle)
    let res = await dispatch(addArticleThunk(newArticle));
    console.log("SUCCESS?", res)
    if(res.message === "success") reset()

    // if(data.errors) return setErrors(data.errors)
      // DATA:  {id: 11, title: 'test', body: 'test', imageUrl: 'test.png'}
    // navigate(`/articles/${data.id}`)
    // reset();
  };



  const reset = () => {
    setTitle('');
    setImageUrl('');
    setBody('');
  };


  return (
    <div className='inputBox'>
      <h1>Create Article</h1>
      {errors.length > 0 && (
        <p style={{color: "red"}}>{errors[0]}</p>
      )}
      <form onSubmit={handleSubmit}>
        <input
          type='text'
          onChange={(e) => setTitle(e.target.value)}
          value={title}
          placeholder='Title'
          name='title'
        />
        <input
          type='text'
          onChange={(e) => setImageUrl(e.target.value)}
          value={imageUrl}
          placeholder='Image URL'
          required
          name='imageUrl'
        />
        <textarea
          value={body}
          onChange={(e) => setBody(e.target.value)}
          name='body'
          placeholder='Add your entry'
          rows='10'
        ></textarea>
        <button type='submit'>Submit</button>
      </form>
    </div>
  );
};

export default ArticleInput;
