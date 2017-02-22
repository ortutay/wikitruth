import React from 'react';

import { url, json } from '../utils/util';


export default class Claims extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      claims: [],
      suggestions: [],
    };
  }

  componentDidMount() {
    console.log('url', url('/claims/search'));
    fetch(url('/claims/search'))
      .then(resp => json(resp))
      .then((data) => {
        console.log('data', data);
        this.setState({ suggestions: data.results })
      });
  }

  addCitation(e) {
    e.preventDefault();
    console.log(this.refs.claim.value);
    let id = this.refs.claim.value;
    for (let claim of this.state.claims) {
      if (id == claim.id) {
        return;
      }
    }
    let claim;
    for (let suggestion of this.state.suggestions) {
      if (suggestion.id == id) {
        claim = suggestion;
      }
    }
    console.log('claim', claim);
    let claims = this.state.claims;
    claims.push(claim);
    this.setState({ claims: claims });
  }

  removeCitation(e, id) {
    e.preventDefault();
    let claims = [];
    for (let claim of this.state.claims) {
      if (claim.id == id) {
        continue;
      }
      claims.push(claim);
    }
    this.setState({ claims: claims });
  }

  renderClaims() {
    let claims = [];
    for (let i = 0; i < this.state.claims.length; i++) {
      let claim = this.state.claims[i];
      claims.push(
        <div key={claim.id}>
          <input type="hidden" name="citations" value={claim.id} />
          {claim.id} - {claim.thesis}
          <button onClick={(e) => this.removeCitation(e, claim.id)}>Remove</button>
        </div>
      );
    }
    return <div>{claims}</div>;
  }

  renderForm() {
    let options = [];
    for (let claim of this.state.suggestions) {
      options.push(
        <option key={claim.id} value={claim.id}>
          {claim.id} - {claim.thesis}
        </option>
      );
    }
    return (
      <div>
        <select ref="claim">{options}</select>
        <button onClick={(e) => this.addCitation(e)}>Add</button>
      </div>
    );
  }

  render() {
    return (
      <div>
        {this.renderClaims()}
        {this.renderForm()}
      </div>
    );
  }
}
