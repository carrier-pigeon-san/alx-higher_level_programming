#!/usr/bin/node
const { argv: args } = require('node:process');

const message1 = 'No argument';
const message2 = 'Argument found';
const message3 = 'Arguments found';

if (args.length > 3) {
  console.log(message3);
} else if (args.length > 2) {
  console.log(message2);
} else {
  console.log(message1);
}
