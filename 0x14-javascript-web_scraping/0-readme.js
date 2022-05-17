#!/usr/bin/node
/* Reads in utf8 from an api using axios module */
const fs = require('fs');
const process = require('process');

fs.readFile(process.argv[2], 'utf8', (err, data) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(data);
});
