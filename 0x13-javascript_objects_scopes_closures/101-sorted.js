#!/usr/bin/node
const dict = require('./101-data').dict;
const new_dict = {};

console.log(dict);
for (const [key, value] of Object.entries(dict)) {
  if (new_dict[value]) {
    new_dict[value].push(key);
  } else {
    new_dict[value] = [key];
  }
}
console.log(new_dict);
