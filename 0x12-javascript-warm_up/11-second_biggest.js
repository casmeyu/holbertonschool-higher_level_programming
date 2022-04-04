#!/usr/bin/node
const numbers = [];

for (let i = 2; process.argv[i]; i++) {
  numbers.push(parseInt(process.argv[i]));
}
numbers.sort((a, b) => { return (b - a); });
console.log(numbers[1]);
