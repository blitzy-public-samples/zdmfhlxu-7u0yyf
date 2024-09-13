import React, { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import { Provider } from 'react-redux';
import App from 'frontend/src/app';
import store from 'frontend/src/store';

const rootElement = document.getElementById('root');
const root = createRoot(rootElement!);

function renderApp() {
  root.render(
    <StrictMode>
      <Provider store={store}>
        <App />
      </Provider>
    </StrictMode>
  );
}

renderApp();