import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import ResultsProvider from './context/ResultsContext';
import './index.css';

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <ResultsProvider>
      <App />
    </ResultsProvider>
  </React.StrictMode>
);
