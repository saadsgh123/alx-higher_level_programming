#!/usr/bin/node
const fs = require('fs');
const fileCame = process.argv[2];
try {
  const output = fs.readFileSync(fileCame, 'utf8');
  console.log(output);
} catch (err) {
  console.error(err);
}
