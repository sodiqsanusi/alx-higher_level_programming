#!/usr/bin/node
const parsed = parseInt(process.argv[2]);
if (!parsed) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  while (i < parsed) {
    console.log('C is fun');
    i++;
  }
}
