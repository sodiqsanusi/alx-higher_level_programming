#!/usr/bin/node

/*
* Use data from a GET request to make other conclusions
*/

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
    process.exitCode = 1;
    return;
  }
  films = JSON.parse(body).results;
  const wedgeAntillesMovies = films.filter((film) => {
    return film.characters.some((character) => {
      return character.endsWith('/18/');
    });
  });
  console.log(wedgeAntillesMovies.length);
});
