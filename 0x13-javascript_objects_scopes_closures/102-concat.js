#!/usr/bin/node
const fs = require('fs');

if (process.argv.length === 5) {
  for (let idx = 2; idx < 4; idx++) {
    let content = '';
    fs.readFile(process.argv[idx], 'utf8', (err, data) => {
      if (err) {
        console.error(err);
        return;
      }

      content = data;

      fs.writeFile(process.argv[4], content, { flag: 'a+' }, (err) => {
        if (err) {
          console.log(err);
        }
      });
    });
  }
}
