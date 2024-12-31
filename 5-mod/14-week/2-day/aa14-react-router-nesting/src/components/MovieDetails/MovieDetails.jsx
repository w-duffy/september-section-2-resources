import { useParams } from "react-router-dom";

function MovieDetails(props) {
  const { movieId } = useParams();

  const movieChoice = props.movies.find((movie) => movie.id === +movieId);
//spots/50
  return (
    <div key={movieId} className="comp purple">
      <h1>{movieChoice.title}</h1>
      <p>{movieChoice.description}</p>
    </div>
  );
}

export default MovieDetails;
