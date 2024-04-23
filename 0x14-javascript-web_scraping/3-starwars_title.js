#!/usr/bin/node

/*
* Print detail from a API
* */

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
    process.exitCode = 1;
  }
  const finalResponse = JSON.parse(body);
  console.log(finalResponse.title);
});
