#!/usr/bin/node
exports.callMeMoby = function callMeMoby (x, theFunction) {
  let num = parseInt(x);
  if (!isNaN(num) && num > 0) {
    while (num > 0) {
      theFunction();
      num--;
    }
  }
};
