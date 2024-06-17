#!/usr/bin/node
const { argv } = require('node:process');

if (argv.length === 2 || argv.length === 3) {
  console.log(0);
} else {
  let largest = parseInt(argv[2]);
  let second = parseInt(argv[2]);
  argv.slice(2).forEach(element => {
    if (parseInt(element) > largest) {
      largest = parseInt(element);
    }
  });

  argv.slice(2).forEach(element => {
    if (parseInt(element) < largest && parseInt(element) > second) {
      second = parseInt(element);
    }
  });

  console.log(second);
}
