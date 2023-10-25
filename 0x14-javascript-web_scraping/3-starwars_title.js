#!/usr/bin/node
const r = require('request');
const url = 'https://swapi-api.alx-tools.com/api/planets/1/' + process.argv[2];

r.get(url, (err, res, body) => {
  if (err) console.log(err);
  else console.log(JSON.parse(body).title);
});
