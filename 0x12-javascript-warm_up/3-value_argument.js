#!/usr/bin/node

// Get the arguments passed to the script
const args = process.argv.slice(2);

// Check if an argument was passed and print the appropriate message
const firstArg = args[0];
if (firstArg === undefined) {
  console.log('No argument');
} else {
  console.log(firstArg);
}
