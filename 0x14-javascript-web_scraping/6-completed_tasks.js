#!/usr/bin/node
/* Prints a json object with each user id and the number of finished tasks */
const axios = require('axios').default;
const process = require('process');

if (process.argv.length >= 3) {
  const url = process.argv[2];

  axios.get(url)
    .then((response) => {
      const taskDict = {};
      response.data.forEach((task) => {
        if (task.completed === true) {
          if (taskDict[task.userId] !== undefined) {
            taskDict[task.userId] += 1;
          } else {
            taskDict[task.userId] = 1;
          }
        }
      });
      console.log(taskDict);
    })
    .catch((error) => {
      console.log(error);
    });
}
