#!/usr/bin/node

const { argv } = require('node:process');
const argNumber = parseInt(argv[2]);

if (Number.isInteger(argNumber)) {
  for (let i = 0; i < argNumber; i++) {
    console.log(Array(argNumber + 1).join('X'));
  }
} else {
  console.log('Missing size');
}
