#!/usr/bin/node

const num = parseInt(process.argv[2]);
let facto = num;

function factorial (num) {
  facto = facto * (num - 1);
  num = num - 1;
  if (num > 1) {
    factorial(num);
  }
}

if (isNaN(num) || num === 1) {
  console.log('1');
} else {
  factorial(num);
  console.log(facto);
}
