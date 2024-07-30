#!/usr/bin/node

// Get the arguments passed to the script
const args = process.argv.slice(2);

// Print the two arguments in the format " is "
const arg1 = args[0];
const arg2 = args[1];
console.log(`${arg1} is ${arg2}`);
