#!/usr/bin/node
const request = require('request');

request(process.argv[2], (err, response, body) => {
  if (err === null) {
    const bodyJson = JSON.parse(body);
    let number = 0;
    for (const x in bodyJson.results) {
      const sentence = bodyJson.results[x];
      for (const charindex in sentence.characters) {
        const character = sentence.characters[charindex];
        if (character.endsWith('/18/')) {
          number += 1;
        }
      }
    }
    console.log(number);
  }
});
