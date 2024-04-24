#!/usr/bin/node

/*
* Make computations from results gotten from a GET request
*/

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  const data = JSON.parse(body);
  const finalObj = {};
  for (const todo of data) {
    if (!(todo.userId in finalObj)) {
      finalObj[todo.userId] = 0;
    }
    if (todo.completed) {
      finalObj[todo.userId] += 1;
    }
  }
  console.log(finalObj);
});
