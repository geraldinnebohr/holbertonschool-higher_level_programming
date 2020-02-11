#!/usr/bin/node
const fs = require('fs');
const data = process.argv[2];
fs.writeFile('my_file.txt', data, (err) => {
  if (err) console.log(err);
});
