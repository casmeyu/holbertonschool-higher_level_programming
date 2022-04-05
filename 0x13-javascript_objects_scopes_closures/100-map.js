#!/usr/bin/node
const data = require('./100-data').list;

console.log(data);
const new_data = data.map((item) => item * 2);
console.log(new_data);
