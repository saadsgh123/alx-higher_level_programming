#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  for (i = 0; i < Number(process.argv[2]); i++) {
    console.log('C is fun');
  }
}
