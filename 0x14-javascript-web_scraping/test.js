#!/usr/bin/node
const request = require('request');

// URL to make the GET request to
const url = 'https://swapi-api.alx-tools.com/api/films';

// Make a GET request
request(url, { json: true }, (error, response, body) => {
  if (error) {
    console.error('Error with the request:', error);
    return;
  }
  console.log(body);
});
