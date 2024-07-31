#!/usr/bin/node

// Get the first argument passed to the script
const arg = process.argv[2];

// Convert the argument to an integer
const size = parseInt(arg);

// Check if the conversion was successful and size is a positive integer
if (isNaN(size) || size <= 0) {
  console.log('Missing size');
} else {
  // Print the square of 'X' characters
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}