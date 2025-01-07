import './SingleArticle.css';
import { useParams } from 'react-router-dom';
import { useSelector } from 'react-redux';

const SingleArticle = () => {
    const { id } = useParams();
    const allArticles = useSelector((store) => store.articleState.entries);

    const article = allArticles.find((el) => el.id === id);

    return (
        <div className="singleArticle">
            {article ? (
                <>
                    <h1>{article.title}</h1>
                    <img src={article.imageUrl} alt={article.title} />
                    <p>{article.body}</p>
                </>
            ) : (
                <h1>Loading...</h1>
            )}
        </div>
    );
};

export default SingleArticle;
