#!/usr/bin/node
const args = process.argv.slice(2);
let count = 0
if (args[0] === undefined) {
    console.log("No argument");
} else {
    while (args[count] !== undefined) {
        console.log(args[count]);
        count++;
    }
}
