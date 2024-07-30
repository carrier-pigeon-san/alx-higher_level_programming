#!/usr/bin/node
const process = require('node:process');
const args = process.argv;
const request = require('request');
const endpoint = 'https://swapi-api.alx-tools.com/api/films';

request.get(`${endpoint}/${args[2]}`, (error, response, body) => {
  if (error) {
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    process.exit(1);
  }

  try {
    const film = JSON.parse(body);
    console.log(film.title);
  } catch (e) {
    process.exit(1);
  }
});
