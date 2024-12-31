import { createBrowserRouter, RouterProvider, NavLink, Outlet } from 'react-router-dom';
import Home from './components/Home';
import Stocks from './components/Stocks';
import Movies from './components/Movies';

import MovieDetails from './components/MovieDetails';
import { movies } from './data/movieData';


function Layout() {
  return (
    <div className='app'>
      <h1>App Component</h1>
      <nav className='comp nav'>
        <ul>
          <li>
            <NavLink
              to='/'
              className={({isActive}) => isActive? 'purple' : ''}
              style={({isActive}) => isActive? { fontWeight: 'bold' } : {}}
            >
              Home
            </NavLink>
          </li>
          <li>
            <NavLink
              to='/stocks'
              className={({isActive}) => isActive? 'purple' : ''}
              style={({isActive}) => isActive? { fontWeight: 'bold' } : {}}
            >
              Stocks
            </NavLink>
          </li>
          <li>
            <NavLink
              to='/movies'
              className={({isActive}) => isActive? 'purple' : ''}
              style={({isActive}) => isActive? { fontWeight: 'bold' } : {}}
            >
              Movies
            </NavLink>
          </li>
        </ul>
      </nav>
      <main>
        <Outlet />
      </main>
    </div>
  );
}

// // Faking a network request ("fetching from the server")
// Just for demonstration
// async function getMoviesFromOhio(){
//   let data = new Promise(res =>{
//     setTimeout(() => {
//       res(movies)
//     }, 250)
//   })
//   return data
// }

const router = createBrowserRouter([
  {
    element: <Layout />,
    children: [
      {
        path: '/',
        element: <Home />
      },
      {
        path: 'stocks',
        element: <Stocks />
      },
      // http://localhost:5173/movies
      // http://localhost:5173/movies/1
      {
        path: 'movies',
        // Docs on line 78: https://reactrouter.com/en/main/hooks/use-loader-data
        // https://youtu.be/95B8mnhzoCM?t=99
        // loader: async () => await getMoviesFromOhio(),
        element: <Movies movies={movies} another={{object: "cool"}} hello="world"  />,
        children: [
          {
            path: ':movieId',
            element: <MovieDetails movies={movies} />
          },
        ]
      },
      {
        path: '*',
        element: <h1>Page Not Found</h1>
      },
      {
        path: '/not-logged-in',
        element: <h1> You Must Be Logged In To Enter.</h1>
      }
    ]
  }
]);

function App() {
  return <RouterProvider router={router} />
}

export default App;
