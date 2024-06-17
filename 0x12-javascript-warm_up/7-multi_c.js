#!/usr/bin/node
const { argv } = require('node:process');

const count = parseInt(argv[2]);

if (Number.isInteger(count)) {
  for (let index = 0; index < count; index++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
