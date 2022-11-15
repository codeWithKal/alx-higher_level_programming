#!/usr/bin/node
const request = require('request');
const URL = process.argv[2];

request(URL, (err, response, body) => {
  if (err === null) { console.log('code: ' + response.statusCode); }
});
