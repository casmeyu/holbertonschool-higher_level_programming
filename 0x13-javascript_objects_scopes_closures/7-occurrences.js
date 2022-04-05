#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let cont = 0;
  for (let idx = 0; list[idx]; idx++) {
    if (list[idx] == searchElement) {
      cont++;
    }
  }
  return (cont);
}
