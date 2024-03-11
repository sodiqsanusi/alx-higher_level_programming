#!/usr/bin/node
function addMeMaybe (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction(x + 1);
  }
}
module.exports = { addMeMaybe };
