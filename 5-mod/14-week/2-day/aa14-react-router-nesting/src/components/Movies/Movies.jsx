import { Outlet } from "react-router-dom";
import MovieNavBar from "./MovieNavBar";

function Movies({ movies, another }) {


  return (
    <div className="comp orange">
      <h1>{another.object}</h1>
      <MovieNavBar movies={movies} />
      <Outlet />
    </div>
  );
}

export default Movies;
