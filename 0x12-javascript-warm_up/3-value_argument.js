#!/usr/bin/node

if (process.argv.length === 3) {
  console.log(process.argv[2]);
}

if (process.argv.length > 3) {
  let i = 2;

  while (i < process.argv.length) {
    console.log(process.argv[i]);
    i++;
  }
}
