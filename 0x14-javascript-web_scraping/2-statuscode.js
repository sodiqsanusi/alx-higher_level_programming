#!/usr/bin/node

/*
* Display the status code of an HTTP GET request
* */

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
    process.exitCode = 1;
  }
  console.log('code:', response.statusCode);
});
