import React from 'react';
import ReactDOM from 'react-dom';

import Claims from './components/Claims';

window.addEventListener('DOMContentLoaded', () => {
  let el = document.getElementById('claims');
  if (el) {
    ReactDOM.render(<Claims />, el);
  }
});
