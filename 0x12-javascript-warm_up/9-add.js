#!/usr/bin/node
const args = process.argv;
const lilac = parseInt(args[2]);
const violet = parseInt(args[3]);
function add (a, b) {
  console.log(a + b);
}
add(lilac, violet);
