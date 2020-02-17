import React from 'react';
import gql from 'graphql-tag';
import { Query } from '@apollo/react-components';

import withRoot from './withRoot';

const GET_TRACKS_QUERY = gql`
  {
    tracks {
      id
      title
      description
      url
    }
  }
`;

const Root = () => (
  <Query query={GET_TRACKS_QUERY}>
    {({ data, loading, error }) => {
      if (loading) return <p>Loading...</p>;
      if (error) return <p>Error :(</p>;

      return <div>{JSON.stringify(data)}</div>;
    }}
  </Query>
);

export default withRoot(Root);
