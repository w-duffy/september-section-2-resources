import { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { NavLink } from 'react-router-dom';
import { loadArticles, articleKilla } from '../../store/articleReducer';
import { fruitKilla } from '../../store/fruitReducer';

const ArticleList = () => {
    const dispatch = useDispatch();
    const articles = useSelector((state) => state.articleState.entries);

    useEffect(() => {
        dispatch(loadArticles());
    }, [dispatch]);

    return (
        <div>
            <button onClick={() => dispatch(articleKilla())}>
                Delete All Articles
            </button>
            <button onClick={() => dispatch(fruitKilla())}>
                Delete All Fruits
            </button>

            <h1>Article List</h1>
            <ol>
                {articles.map(({ id, title }) => (
                    <li key={id}>
                        <NavLink to={`${id}`}>{title}</NavLink>
                    </li>
                ))}
            </ol>
        </div>
    );
};

export default ArticleList;
