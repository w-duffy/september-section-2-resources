import './App.css';
import { createBrowserRouter, RouterProvider, Outlet } from 'react-router-dom';
import NavBar from './components/NavBar';
import FunctionalComponent from './components/FunctionalComponent';
import ClassComponent from './components/ClassComponent';
import Kahoot from './components/Kahoot';
import KahootOne from './components/Kahoot/One';
import KahootTwo from './components/Kahoot/Two';
import KahootThree from './components/Kahoot/Three';
import KahootFour from './components/Kahoot/Four';

const Layout = () => {
    return (
        <main>
            <NavBar />
            <Outlet />
        </main>
    );
};

/** //? My preference, doesn't really matter tho :)
const router = createBrowserRouter([
{
    element: <Layout />,
    children: [
        {
            path: '/',
            element: <h1>Home</h1>,
        },
 */

const router = createBrowserRouter([
    {
        path: '/',
        element: <Layout />,
        children: [
            {
                index: true,
                element: <h1>Home</h1>,
            },
            {
                path: '/function',
                element: <FunctionalComponent />,
            },
            {
                path: '/class',
                element: <ClassComponent />,
            },
            {
                path: '/kahoot',
                element: <Kahoot />,
                // children: [
                //     {
                //         path: '1',
                //         element: <div>Kahoot 1</div>,
                //     },
                //     {
                //         path: '2',
                //         element: <div>Kahoot 2</div>,
                //     },
                //     {
                //         path: '3',
                //         element: <div>Kahoot 3</div>,
                //     },
                //     {
                //         path: '4',
                //         element: <div>Kahoot 4</div>,
                //     },
                // ],
            },
            {
                path: '/kahoot/1',
                element: <KahootOne value="Momo" />,
            },
            {
                path: '/kahoot/2',
                element: <KahootTwo />,
            },
            {
                path: '/kahoot/3',
                element: <KahootThree />,
            },
            {
                path: '/kahoot/4',
                element: <KahootFour />,
            },
        ],
    },
]);

function App() {
    return <RouterProvider router={router} />;
}

export default App;
