#!/usr/bin/node
const { argv } = require('node:process');

const message = 'No argument';

if (argv[2]) {
  console.log(argv[2]);
} else {
  console.log(message);
}
