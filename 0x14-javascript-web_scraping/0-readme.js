#!/usr/bin/node

/* Read and print the content of a file
* The filename will be passed as a terminal argument
*/

const fs = require('fs');
const filename = process.argv[2];

fs.readFile(filename, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
