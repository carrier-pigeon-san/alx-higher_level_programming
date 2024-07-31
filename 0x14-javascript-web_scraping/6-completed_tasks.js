#!/usr/bin/node
const process = require('node:process');
const args = process.argv;
const request = require('request');

request.get(args[2], { json: true }, (err, response, body) => {
  if (err) {
    console.log(err);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.log('Code: ', response.statusCode);
    process.exit(1);
  }

  try {
    const done = {};

    body.forEach((item) => {
      if (item.completed === true) {
        const index = String(item.userId);
        if (Object.prototype.hasOwnProperty.call(done, index)) {
          done[index] += 1;
        } else {
          done[index] = 1;
        }
      }
    });
    console.log(done);
  } catch (e) {
    console.log('Caught: ', e);
    process.exit(1);
  }
});
