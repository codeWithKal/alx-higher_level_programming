#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const path = process.argv[3];
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error === null) {
    const content = body;
    fs.writeFile(path, content, (err) => {
      if (err) console.log(err);
    });
  }
});
