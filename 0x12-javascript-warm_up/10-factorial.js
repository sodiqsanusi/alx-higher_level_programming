#!/usr/bin/node
const parsed = parseInt(process.argv[2]);
function factorial (factor) {
  if (isNaN(factor)) {
    return (1);
  } else if (factor === 1) {
    return (1);
  }
  return (factor * factorial(factor - 1));
}
console.log(factorial(parsed));
