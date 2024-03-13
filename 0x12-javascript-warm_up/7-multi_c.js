#!/usr/bin/node

const { argv } = require('node:process');
const argNumber = parseInt(argv[2]);

if (Number.isInteger(argNumber)) {
  for (let i = 0; i < argNumber; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
