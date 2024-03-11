#!/usr/bin/node
const args = process.argv;
if (args.length < 4) {
  console.log(0);
} else {
  const parsedArr = [];
  for (let i = 2; i < args.length; i++) {
    parsedArr.push(parseInt(args[i]));
  }
  parsedArr.sort((a, b) => b - a);
  console.log(parsedArr[1]);
}
