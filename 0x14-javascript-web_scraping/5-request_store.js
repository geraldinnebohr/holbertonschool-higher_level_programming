#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const file = process.argv[3];

request.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(file, body, (err) => {
      if (err) console.log(err);
    });
  }
});
