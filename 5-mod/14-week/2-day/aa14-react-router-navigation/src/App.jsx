import {
  createBrowserRouter,
  RouterProvider,
  // Link,
  NavLink,
  Outlet,
} from "react-router-dom";
import Home from "./components/Home";
import Stocks from "./components/Stocks";
import Movies from "./components/Movies";

function Navigation() {
  return (
    <nav className="comp nav">
      <ul>
        <li>
          <NavLink
            style={({ isActive }) => {
              return { fontWeight: isActive ? "bold" : "" };
            }}
            to="/"
          >
            Home
          </NavLink>
        </li>
        <li>
          <NavLink
            style={({ isActive }) => {
              return { fontWeight: isActive ? "bold" : "" };
            }}
            to="/stocks"
          >
            Stocks
          </NavLink>
        </li>
        <li>
          <NavLink to="/movies">Movies</NavLink>
        </li>
        <li>
          <a href="/stocks">Stocks A Tag</a>
        </li>
      </ul>
    </nav>
  );
}
const Layout = () => {
  return (
    <div className="app">
      <h1>App Component</h1>
      <nav>
        <Navigation />
      </nav>
      <main style={{height:300,width:300,borderRadius:'50%'}}>

        <Outlet />
      </main>
    </div>
  );
};

const router = createBrowserRouter([
  {
    element: <Layout />,
    children: [
      {
        path: "/home",
        element: <Home />,
        children: [
          {
            path: "example",
            element: <h1>Example</h1>,
          }
        ]
      },
      {
        path: "stocks",
        element: <Stocks />,
      },
      {
        path: "movies",
        element: <Movies />,
      },
      {
        path: "/not-logged-in",
        element: <h1>You Must Be Logged In To Enter.</h1>,
      },
      {
        path: "*",
        element: <h1>Page Not Found</h1>,
      },
    ],
  },
]);

function App() {
  return <RouterProvider router={router} />;
}

export default App;
