#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/planets/1/${id}`;

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  }
  console.log(JSON.parse(body).title);
});
