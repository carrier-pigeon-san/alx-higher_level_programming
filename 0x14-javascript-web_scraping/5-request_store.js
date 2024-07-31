#!/usr/bin/node
const process = require('node:process');
const args = process.argv;
const request = require('request');
const fs = require('fs');

request.get(args[2], (error, response, body) => {
  if (error) {
    console.log(error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.log('code:', response.statusCode);
    process.exit(1);
  }

  try {
    fs.writeFile(args[3], body, (err) => {
      if (err) {
        console.log(err);
        process.exit(1);
      }
    });
  } catch (e) {
    console.log(e);
    process.exit(1);
  }
});
