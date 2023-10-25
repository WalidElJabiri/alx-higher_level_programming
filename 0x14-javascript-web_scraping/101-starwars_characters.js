#!/usr/bin/node
const request = require('request');
const fId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${fId}`;

request(url, async function (err, response, body) {
  if (err) {
    console.log(err);
  }
  for (const cId of JSON.parse(body).characters) {
    await new Promise((resolve, reject) => {
      request(cId, function (err, response, body) {
        if (err) {
          reject(err);
        } else {
          console.log(JSON.parse(body).name);
          resolve();
        }
      });
    });
  }
});
