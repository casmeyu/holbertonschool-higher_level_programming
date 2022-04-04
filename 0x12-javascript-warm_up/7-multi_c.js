#!/usr/bin/node
let num = parseInt(process.argv[2]);
if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else if (num > 0) {
  while (num !== 0) {
    console.log('C is fun');
    num--;
  }
}
