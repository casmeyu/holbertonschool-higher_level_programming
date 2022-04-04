#!/usr/bin/node
let max, sMax;

if (process.argv.length < 4) {
  console.log(0);
} else {
  max = parseInt(process.argv[2]);
  sMax = parseInt(process.argv[2]);
  for (let idx = 2; process.argv[idx]; idx++) {
    if (parseInt(process.argv[idx]) > max) {
      sMax = max;
      max = parseInt(process.argv[idx]);
    }
  }
  console.log(sMax);
}
