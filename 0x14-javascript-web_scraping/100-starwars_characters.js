#!/usr/bin/node
const request = require('request');
const fId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${fId}`;

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  }
  for (const cId of JSON.parse(body).characters) {
    request(cId, function (err, response, body) {
      if (err) {
        console.log(err);
      }
      console.log(JSON.parse(body).name);
    });
  }
});
