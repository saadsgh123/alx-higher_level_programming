#!/usr/bin/node
function factorialIterative (n) {
  if (n < 0) {
    return undefined;
  }

  let result = 1;
  for (let i = 1; i <= n; i++) {
    result *= i;
  }

  return result;
}
console.log(factorialIterative(Number(process.argv[2])));
