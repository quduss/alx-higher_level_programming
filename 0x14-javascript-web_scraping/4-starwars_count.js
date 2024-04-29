#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request.get(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const movies = JSON.parse(body).results;
    const count = movies.reduce((acc, movie) => {
      if (movie.characters.some(characterUrl => characterUrl.endsWith('/18/'))) {
        return acc + 1;
      }
      return acc;
    }, 0);
    console.log(`${count}`);
  }
});
