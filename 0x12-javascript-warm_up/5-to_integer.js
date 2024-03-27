#!/usr/bin/node
const parsed = parseInt(process.argv[2]);
if (!parsed) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parsed);
}
