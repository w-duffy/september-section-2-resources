import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import sampleData from './assets/sample.json';
import spiData from './assets/spi.json';
import bonusData from './assets/bonus.json';
import HomePage from './components/HomePage';
import Navigation from './navigation';
import SurveyPage from './components/SurveyPage';
import ReportPage from './components/ReportPage';
import NotFoundPage from './components/NotFoundPage';

const router = createBrowserRouter([
  {
    element: <Navigation />,
    children: [
      {
        path: '/',
        element: <HomePage />
      },
      {
        path: 'sample',
        element: <SurveyPage survey={sampleData} />
      },
      {
        path: 'spi',
        element: <SurveyPage survey={spiData} />
      },
      {
        path: 'likert',
        element: <SurveyPage survey={bonusData} />
      },
      {
        path: 'report',
        element: <ReportPage />
      },
      {
        path: '*',
        element: <NotFoundPage />
      }
    ]
  }
]);

function App() {
  return <RouterProvider router={router} />;
}

export default App;

