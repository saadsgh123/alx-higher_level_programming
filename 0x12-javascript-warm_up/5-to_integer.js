#!/usr/bin/node
const args = process.argv.slice(2);
if (isNaN(args[0]) || args[0] === undefined) {
  console.log('Not a number');
} else {
  const sentence = parseInt(args[0]);
  console.log('My Number: ', sentence);
}
