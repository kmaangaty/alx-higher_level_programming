#!/usr/bin/node
const rq = require('request');
rq.get(process.argv[2]).on('response', function (rp) {
  console.log(`code: ${rp.statusCode}`);
});
