#!/usr/bin/node

// Function to add two integers
function add (a, b) {
  return a + b;
}

// Get the first and second arguments passed to the script
const firstArg = parseInt(process.argv[2]);
const secondArg = parseInt(process.argv[3]);

// Check if the arguments can be converted to integers and perform the addition
if (isNaN(firstArg) || isNaN(secondArg)) {
  console.log('NaN');
} else {
  console.log(add(firstArg, secondArg));
}
