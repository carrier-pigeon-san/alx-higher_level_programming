#!/usr/bin/node

const { argv } = require('node:process');

if (argv.length < 4) {
  console.log(0);
} else {
  const args = [];
  for (let i = 2; i < argv.length; i++) {
    args.push(parseInt(argv[i]));
  }
  args.sort(function (a, b) {
    return b - a;
  });
  console.log(args[1]);
}
