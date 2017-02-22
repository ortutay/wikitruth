import changeCase from 'change-object-case';

import { API_HOST } from '../config';


export function url(path) {
  return API_HOST + path;
}

export function json(resp) {
  return resp.json()
    .then(data => changeCase.camelKeys(data, {recursive: true, arrayRecursive: true}))
}

export function jsonAndStatus(resp) {
  return resp.json().then(json => { return { status: resp.status, data: json }});
}
