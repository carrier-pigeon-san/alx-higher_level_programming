#!/usr/bin/node

const { argv } = require('node:process');

function add (a, b) {
  const sum = a + b;
  console.log(sum);
}

const a = parseInt(argv[2]);
const b = parseInt(argv[3]);
add(a, b);
