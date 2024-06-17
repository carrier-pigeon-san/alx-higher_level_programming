#!/usr/bin/node
const { argv } = require('node:process');

const toInt = parseInt(argv[2]);

if (Number.isInteger(toInt)) {
  console.log('My number:', toInt);
} else {
  console.log('Not a number');
}
