#!/usr/bin/node
const data = require('./100-data').list;

console.log(data);
const new_data = data.map((item, idx) => item * idx);
console.log(new_data);
