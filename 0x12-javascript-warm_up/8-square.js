#!/usr/bin/node
const parsed = parseInt(process.argv[2]);
if (!parsed) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parsed; i++) {
    console.log('X'.repeat(parsed));
  }
}
