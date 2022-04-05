#!/usr/bin/node
const data = require('./100-data').list;

console.log(data);
const newData = data.map((item, idx) => item * idx);
console.log(newData);
