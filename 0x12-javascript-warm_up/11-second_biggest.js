#!/usr/bin/node
const numbers = process.argv.slice(2);
const sortedNumbers = numbers.sort();
if (sortedNumbers.length <= 1) {
  console.log(0);
} else {
  console.log(sortedNumbers[numbers.length - 2]);
}
