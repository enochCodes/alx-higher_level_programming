#!/usr/bin/node

// Function to compute factorial recursively
function factorial(n) {
  if (isNaN(n) || n === 0) {
    return 1;
  }
  return n * factorial(n - 1);
}

// Get the first argument passed to the script and cast it to an integer
const arg = parseInt(process.argv[2]);

// Compute and print the factorial
console.log(factorial(arg));
