#!/usr/bin/node
const process = require('node:process');
const args = process.argv;
const request = require('request');
const endpoint = `https://swapi-api.alx-tools.com/api/films/${args[2]}`;

request.get(endpoint, { json: true }, (err, response, body) => {
  if (err) {
    console.log('Error: ', err);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.log('Code: ', response.statusCode);
    process.exit(1);
  }

  try {
    body.characters.forEach((item) => {
      request.get(item, { json: true }, (err1, response1, body1) => {
        if (err1) {
          console.log('Error 1: ', err1);
          process.exit(1);
        }

        if (response1.statusCode !== 200) {
          console.log('Code 1: ', response1.statusCode);
          process.exit(1);
        }

        try {
          console.log(body1.name);
        } catch (e1) {
          console.log('Caught 1: ', e1);
          process.exit(1);
        }
      });
    });
  } catch (e) {
    console.log('Caught: ', e);
    process.exit(1);
  }
});
