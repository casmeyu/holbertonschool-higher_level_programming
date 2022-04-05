#!/usr/bin/node
exports.addMeMaybe = function addMeMaybe (x, theFunction) {
  const num = parseInt(x);
  if (!isNaN(num)) {
    theFunction(num + 1);
  }
};
