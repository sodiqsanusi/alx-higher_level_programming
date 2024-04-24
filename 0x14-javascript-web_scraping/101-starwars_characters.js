#!/usr/bin/node

/*
* From the result gotten from a GET request, make other requests
*/

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
    process.exitCode = 1;
    return;
  }
  const data = JSON.parse(body).characters;
  for (const character of data) {
    request(character, function (error, response, body) {
      if (error) {
        console.error(error);
        process.exitCode = 1;
        return;
      }
      const name = JSON.parse(body).name;
      console.log(name);
    });
  }
});
