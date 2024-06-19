#!/usr/bin/node
const list = require('./100-data.js').list;
let index = 0;
const mutList = list.map((ele) => (ele * index++));
console.log(list);
console.log(mutList);
