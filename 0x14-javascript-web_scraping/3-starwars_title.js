#!/usr/bin/node
const url = 'https://swapi-api.hbtn.io/api/films/';
const en = process.argv[2];
const rq = require('request');
rq(url + en, function (err, rp, pd) {
  if (err) {
    console.log(err);
  } else if (rp.statusCode === 200) {
    const rpj = JSON.parse(pd);
    console.log(rpj.title);
  } else {
    console.log('Error code: ' + rp.statusCode);
  }
});
