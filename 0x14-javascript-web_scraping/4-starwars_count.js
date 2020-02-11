#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let count = 0;
    const results = JSON.parse(body).results;
    results.forEach(function (result) {
      const characters = result.characters;
      characters.forEach(function (character) {
        if (character.includes('/18')) {
          count++;
        }
      });
    });
    console.log(count);
  }
});
