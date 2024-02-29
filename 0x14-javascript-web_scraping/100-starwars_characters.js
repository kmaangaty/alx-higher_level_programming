#!/usr/bin/node

const rq = require('request');
const uid = process.argv[2];
const rul = 'https://swapi-api.hbtn.io/api/films/';
rq.get(rul + uid, function (err, rs, bd) {
  if (err) {
    console.log(err);
  }
  const dt = JSON.parse(bd);
  const rud = dt.characters;
  for (const x of rud) {
    rq.get(x, function (errs, rs1, bd1) {
      if (errs) {
        console.log(errs);
      }
      const dt1 = JSON.parse(bd1);
      console.log(dt1.name);
    });
  }
});
