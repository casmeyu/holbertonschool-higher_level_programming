#!/usr/bin/node
/* Returns the name of a starwars film given a movie number */
const axios = require('axios').default;
const process = require('process');

if (process.argv.length >= 3) {
  const url = process.argv[2];
  const search = 'https://swapi-api.hbtn.io/api/people/18/';
  axios.get(url)
    .then((response) => {
      let count = 0;
      response.data.results.forEach((film) => {
        film.characters.forEach((character) => {
          if (character === search) {
            count += 1;
          }
        });
      });
      console.log(count);
    })
    .catch((error) => {
      console.log(0);
    });
}
