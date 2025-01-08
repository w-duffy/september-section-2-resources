import { useParams } from 'react-router-dom';
import { useSelector } from 'react-redux';
import './SingleArticle.css';

const SingleArticle = () => {
  const { id } = useParams();
console.log("In single article")
  const singleArticle = useSelector(state => 
    state.articleState.entries.find(article => article.id === id)
  )


// if(singleArticle === undefined) return <LoadingSpinner />

  return (
    <div className='singleArticle'>
      <h1>{singleArticle?.title}</h1>
      <img
        src={singleArticle?.imageUrl}
        alt={singleArticle?.title}
      />
      <p>
        {singleArticle?.body}
      </p>
    </div>
  );
};

export default SingleArticle;
