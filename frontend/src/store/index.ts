import { createStore, applyMiddleware } from 'redux';
import thunk from 'redux-thunk';
import { composeWithDevTools } from 'redux-devtools-extension';
import { rootReducer } from 'frontend/src/store/reducers';

// Create the Redux store with the root reducer, Redux Thunk middleware,
// and Redux DevTools extension support
const store = createStore(
  rootReducer,
  composeWithDevTools(applyMiddleware(thunk))
);

export default store;