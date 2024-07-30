#!/usr/bin/node
const process = require('node:process');
const args = process.argv;
const request = require('request');

request(args[2], function (error, response, body) {
  if (error) {
    return;
  }
  console.log('code:', response && response.statusCode);
});
