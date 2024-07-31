#!/usr/bin/node

// Get all arguments passed to the script, excluding the first two (node and script path)
const args = process.argv.slice(2).map(Number);

if (args.length <= 1) {
  console.log(0);
} else {
  // Sort the array in descending order and get the second largest unique element
  const uniqueArgs = [...new Set(args)].sort((a, b) => b - a);
  console.log(uniqueArgs[1]);
}
