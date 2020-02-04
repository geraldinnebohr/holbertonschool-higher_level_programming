#!/usr/bin/node
exports.addMeMaybe = function addMeMaybe (number, theFunction) {
  number += 1;
  theFunction(number);
};
