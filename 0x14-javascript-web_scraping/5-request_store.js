#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const path = process.argv[3];
const url = process.argv[2];

request(url, (err, res, body) => {
  if (err === null) {
    const content = body;
    fs.writeFile(path, content, (error) => {
	    if (error)
		    console.log(error);
    });
  }
});
