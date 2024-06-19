#!/usr/local/bin/node
const numbers = process.argv.slice(2);
const sortedNumbers = numbers.sort();
if (sortedNumbers.length <= 0) {
  console.log(sortedNumbers.length);
} else {
  console.log(sortedNumbers[numbers.length - 2]);
}
