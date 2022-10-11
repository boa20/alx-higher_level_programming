#!/usr/bin/node

let num = parseInt(process.argv[2]);
let factorial = num;

if (isNaN(num) || num === 1) {
  console.log('1');
} else {
  while (num > 1) {
    factorial = factorial * (num - 1);
    num = num - 1;
  }
  console.log(factorial);
}
