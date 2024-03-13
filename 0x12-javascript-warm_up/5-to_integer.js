#!/usr/bin/node

const { argv } = require('node:process');
let argNumber = parseInt(argv[2])

if (!Number.isInteger(argNumber)) {
  console.log('Not a number')
} else {
  console.log(`My number: ${argNumber}`);
}
