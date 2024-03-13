#!/usr/bin/node
const count = process.argv.length;
let message = '';
if (count === 0 || count == null) {
  message = 'No argument';
} else if (count === 1) {
  message = 'Argument found';
} else {
  message = 'Arguments found';
}
console.log(message);
