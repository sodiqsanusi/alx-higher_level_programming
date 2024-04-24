#!/usr/bin/node

/*
* From the result gotten from a GET request, make other requests
*/

const request = require('request');
const util = require('util');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;
const requestPromise = util.promisify(request);

request(url, async function (error, response, body) {
  if (error) {
    console.error(error);
    process.exitCode = 1;
    return;
  }
  const data = JSON.parse(body).characters;
  for (const character of data) {
    let response = await requestPromise(character);
    response = JSON.parse(response.body);
    console.log(response.name);
  }
});
