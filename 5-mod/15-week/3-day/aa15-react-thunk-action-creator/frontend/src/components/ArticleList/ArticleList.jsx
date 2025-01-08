import { useDispatch, useSelector } from 'react-redux';
import { useEffect } from 'react';
import { NavLink } from 'react-router-dom';
import { loadArticlesThunk, articleSelector } from '../../store/articleReducer';

const ArticleList = () => {
  const dispatch = useDispatch();
  // const articles = useSelector(state=>state.articleState.entries);
  
    //! Without reselect
    // const articles= Object.values(useSelector((state) => state.articleState.entries));
    // const allArticles= useSelector((state) => state.articleState.entries);
    // const articles = Object.values(allArticles);

  const articles = useSelector(articleSelector);

  
  // console.log("Step 1 Article List Component first Renders")

  useEffect(() => {
    // console.log("Step 2 component has mounted; useEffect runs")
    dispatch(loadArticlesThunk());
  }, [dispatch]);
  
  
  if(articles.length === 0) return null

  console.log("Obj Vals", articles)
  
  // console.log("Step 8 -- FINAL STEP: BACK IN THE COMPONENT; useSelector triggers rerender with latest state")
  return (
    <div>
      <h1>Article List</h1>
      <ol>
        {articles.map(({ id, title }) => (
          <li key={id}><NavLink to={`${id}`}>{title}</NavLink></li>
        ))}
      </ol>
    </div>
  );
};

export default ArticleList;
