#!/usr/bin/node
const dict = require('./101-data.js').dict;

const mutDict = {};

for (const [key, value] of Object.entries(dict)) {
  if (Object.hasOwnProperty.call(mutDict, value)) {
    mutDict[value] = mutDict[value].concat(key);
  } else {
    mutDict[value] = [key];
  }
}

console.log(mutDict);
