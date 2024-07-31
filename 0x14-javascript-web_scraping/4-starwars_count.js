#!/usr/bin/node
const process = require('node:process');
const args = process.argv;
const request = require('request');

request.get(args[2], (error, response, body) => {
  if (error) {
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    process.exit(1);
  }

  try {
    let occurence = 0;
    const films = JSON.parse(body);
    films.results.forEach(element => {
      element.characters.forEach(person => {
        if (person.split('/').includes('18')) {
          occurence += 1;
        }
      });
    });
    console.log(occurence);
  } catch (e) {
    process.exit(1);
  }
});
