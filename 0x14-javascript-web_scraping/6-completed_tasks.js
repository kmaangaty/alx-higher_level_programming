#!/usr/bin/node

const rq = require('request');
const rul = process.argv[2];
rq(rul, function (err, rp, bd) {
  if (err) {
    console.log(err);
  } else if (rp.statusCode === 200) {
    const cm = {};
    const ts = JSON.parse(bd);
    for (const i in ts) {
      const task = ts[i];
      if (task.completed === true) {
        if (cm[task.userId] === undefined) {
          cm[task.userId] = 1;
        } else {
          cm[task.userId]++;
        }
      }
    }
    console.log(cm);
  } else {
    console.log('An error occured. Status code: ' + rp.statusCode);
  }
});
