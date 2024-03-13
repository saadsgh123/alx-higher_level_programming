#!/usr/bin/node
const argument = process.argv;
if (argument.length < 3) {
  console.log('No argument');
} else {
  console.log(argument[2]);
}
