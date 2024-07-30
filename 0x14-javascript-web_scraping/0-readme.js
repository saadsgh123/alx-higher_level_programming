#!/usr/bin/node
const fs = require('fs');
const file_name = process.argv[2];
try {
  const output = fs.readFileSync(file_name, 'utf8');
  console.log(output);
} catch (err) {
  console.error(err);
}
