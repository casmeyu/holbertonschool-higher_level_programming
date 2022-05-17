#!/usr/bin/node
/* List all the characters from a starwars movie based on the id with axios */
const axios = require('axios').default;
const process = require('process');

if (process.argv.length >= 3) {
  const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

  axios.get(url)
    .then((response) => {
      const characters = response.data.characters.sort();
      characters.forEach((charUrl) => {
        // Making asyncronous call to keep the order in the list of characters
        setTimeout(() => {
          axios.get(charUrl)
            .then((charResponse) => {
              console.log(charResponse.data.name);
            })
            .catch((error) => {
              console.log(error);
            });
        }, 100);
      });
    })
    .catch((error) => {
    // handle error
      console.log(error);
    });
}
