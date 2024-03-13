#!/usr/bin/node

const { argv } = require('node:process');
const argNumber = parseInt(argv[2]);

function factorial (n) {
  if (n <= 1 || !Number.isInteger(n)) return 1;
  return n * factorial(n - 1);
}

const result = factorial(argNumber);
console.log(result);
