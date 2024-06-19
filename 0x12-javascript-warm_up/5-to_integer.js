#!/usr/bin/node
const args = process.argv.slice(2);
if (args.length === 0) {
  console.log('Not a number');
} else {
  const sentence = parseInt(args[0]);
  console.log(sentence);
}
