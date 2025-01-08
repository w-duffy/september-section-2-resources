import React from 'react';
import ReactDOM from 'react-dom/client';
//!!START SILENT
import { Provider } from 'react-redux';
import configureStore from './store';
import { populateProduce } from './store/produce';
//!!END
import App from './App';
import './index.css';

//!!START SILENT
const store = configureStore();

if (import.meta.env.MODE !== "production") {
  window.store = store;
  window.populateProduce = populateProduce;
}

//!!END
ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    {/*!!START SILENT */}
    <Provider store={store}>
    {/*!!END */}
      <App />
    {/*!!START SILENT */}
    </Provider>
    {/*!!END */}
  </React.StrictMode>
);

