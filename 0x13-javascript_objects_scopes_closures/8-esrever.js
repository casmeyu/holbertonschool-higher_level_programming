#!/usr/bin/node
exports.esrever = function (list) {
  const revList = [];
  if (list) {
    for (let idx = (list.length - 1); idx >= 0; idx--) {
      revList.push(list[idx]);
    }
  }
  return (revList);
};
