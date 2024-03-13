#!/usr/bin/node
const count = process.argv.length;
let message = '';
if (count < 3 || count == null) {
  message = 'No argument';
} else if (count === 3) {
  message = 'Argument found';
} else {
  message = 'Arguments found';
}
console.log(message);
