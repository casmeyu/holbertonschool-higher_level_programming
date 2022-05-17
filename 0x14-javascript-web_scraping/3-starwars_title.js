#!/usr/bin/node
/* Returns the name of a starwars film given a movie number */
const axios = require('axios').default;
const process = require('process');

if (process.argv.length >= 3) {
  const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;
  axios.get(url)
    .then((response) => {
      console.log(response.data.title);
    })
    .catch((error) => {
      console.log(error);
    });
}
