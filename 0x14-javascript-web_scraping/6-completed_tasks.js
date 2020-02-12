#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const obj = {};
    const todos = JSON.parse(body);
    todos.forEach(task => {
      if (task.completed === true) {
        const k = task.userId;
        if (k in obj) {
          obj[k]++;
        } else {
          obj[k] = 1;
        }
      }
    });
    console.log(obj);
  }
});
