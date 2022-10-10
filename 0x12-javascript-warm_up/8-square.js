#!/usr/bin/node

if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < process.argv[2]; i++) {
    const square = 'X'.repeat(process.argv[2]);
    console.log(square);
  }
}
