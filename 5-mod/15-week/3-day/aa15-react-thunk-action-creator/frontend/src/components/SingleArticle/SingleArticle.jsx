import { useParams } from 'react-router-dom';
import { useSelector } from 'react-redux';
import './SingleArticle.css';

const SingleArticle = () => {
  const { id } = useParams();
  // const singleArticle = useSelector(
    // state => state.articleState.entries.find(article => article.id === id)
  // )
  const singleArticle = useSelector((state) => state.articleState.entries[id]);

  //{"Spots": [{spotId: 1, name: "hi"}, {spotId: 2, name: "bye"}] } /// RIGHT NOW


  // {1: {spotId: 1, name: "hi"}, 2: {spotId: 2, name: "bye"}}



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
