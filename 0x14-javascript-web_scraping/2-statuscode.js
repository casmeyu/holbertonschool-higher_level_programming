#!/usr/bin/node
/* Prints the status of an http request using axios module */
const axios = require('axios').default;
const process = require('process');

if (process.argv.length >= 2) {
  axios.get(process.argv[2])
    .then((response) => {
      console.log(`code: ${response.request.res.statusCode}`);
    })
    .catch((error) => {
      console.log(`code: ${error.request.res.statusCode}`);
    });
}
