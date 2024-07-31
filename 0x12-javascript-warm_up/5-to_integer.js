#!/usr/bin/node

// Get the arguments passed to the script
const args = process.argv.slice(2);

// Get the first argument
const firstArg = args[0];

// Convert the first argument to an integer
const num = parseInt(firstArg);

// Check if the conversion was successful and print the appropriate message
if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${num}`);
}
