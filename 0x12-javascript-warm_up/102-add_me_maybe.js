#!/usr/bin/node
exports.addMeMaybe = addMeMaybe;
function addMeMaybe (number, theFunction) {
  number++;
  theFunction(number);
}
