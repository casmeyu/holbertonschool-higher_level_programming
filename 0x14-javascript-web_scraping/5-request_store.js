#!/usr/bin/node
/* Returns the name of a starwars film given a movie number */
const axios = require('axios').default;
const fs = require('fs');
const process = require('process');

if (process.argv.length >= 4) {
  const url = process.argv[2];
  axios.get(url)
    .then((response) => {
      const content = response.data;
      fs.writeFile(process.argv[3], content, { flag: 'w+' }, (error) => {
        if (error) {
          console.log(error);
        }
      });
    })
    .catch((error) => {
      console.log(error);
    });
}
