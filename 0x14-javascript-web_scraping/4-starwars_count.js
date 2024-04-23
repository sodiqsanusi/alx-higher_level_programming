#!/usr/bin/node

/*
* Use data from a GET request to make other conclusions
*/

const request = require('request');
const url = process.argv[2];
let finalResponse;

const helper = (arr, url) => {
  let count = 0;
  for (const result of arr) {
    const characters = result.characters;
    const test = characters.some((x) => x === url);
    if (test) {
      count++;
    }
  }
  return (count);
};

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
    process.exitCode = 1;
    return;
  }
  finalResponse = JSON.parse(body);
  const person = 'https://swapi-api.alx-tools.com/api/people/18/';
  finalResponse = helper(finalResponse.results, person);
  console.log(finalResponse);
});
