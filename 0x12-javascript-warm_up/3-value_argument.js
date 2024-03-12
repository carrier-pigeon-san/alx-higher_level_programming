#!/usr/bin/node

const { argv } = require('node:process');
const iterator1 = argv[Symbol.iterator]();
let i = 0;

for (const value of iterator1) {
  if (i === 2) {
    console.log(value);
  }
  i++;
}
if (i === 2) {
  console.log('No argument');
}
