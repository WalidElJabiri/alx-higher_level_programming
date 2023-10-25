#!/usr/bin/node
const r = require('request');

r.get(process.argv[2], (err, res, body) => {
  if (err) console.log(err);
  else {
    const computed = {};
    const all = JSON.parse(body);
    all.forEach(task => {
      if (task.completed) {
        if (!computed[task.userId]) computed[task.userId] = 1;
        else computed[task.userId] += 1;
      }
    });
    console.log(computed);
  }
});
