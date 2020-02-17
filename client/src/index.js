import React from 'react';
import ReactDOM from 'react-dom';
import { ApolloProvider } from '@apollo/react-components';
import ApolloClient from 'apollo-boost';

import Root from './Root';

const client = new ApolloClient({
  uri: 'http://localhost:8000/graphql/'
});

ReactDOM.render(
  <ApolloProvider client={client}>
    <Root />
  </ApolloProvider>,
  document.getElementById('root')
);
