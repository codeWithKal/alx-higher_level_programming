#!/usr/bin/node
const request = require('request');
const SITE = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(SITE, (err, response, body) => {
  if (err === null) {
    console.log(JSON.parse(body).title);
  }
});
