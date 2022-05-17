#!/usr/bin/node
/* Reads in utf8 from an api using axios module */
const fs = require('fs');
const process = require('process');

if (process.argv.length >= 4) {
  const content = process.argv[3];
  fs.writeFile(process.argv[2], content, { flag: 'w+' }, (err) => {
    if (err) {
      console.log(err);
    }
  });
}
