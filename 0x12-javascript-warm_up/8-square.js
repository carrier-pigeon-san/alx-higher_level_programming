#!/usr/bin/node
const { argv } = require('node:process');

const dimensions = parseInt(argv[2]);

if (Number.isInteger(dimensions)) {
  let row = '';
  for (let x = 0; x < dimensions; x++) {
    row += 'X';
  }
  for (let y = 0; y < dimensions; y++) {
    console.log(row);
  }
} else {
  console.log('Missing size');
}
