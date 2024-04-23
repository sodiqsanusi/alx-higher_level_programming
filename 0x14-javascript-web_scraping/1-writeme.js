#!/usr/bin/node

/* Write string content to a file
* The filename will be passed as a terminal argument
* The string content will also be passed as a terminal argument
*/

const fs = require('fs');
const filename = process.argv[2];
const stringContent = process.argv[3];

fs.writeFile(filename, stringContent, 'utf8', (err) => {
  if (err) {
    console.error(err);
  }
});
