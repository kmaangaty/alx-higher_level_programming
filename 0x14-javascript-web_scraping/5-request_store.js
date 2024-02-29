#!/usr/bin/node
const fd = require('fs');
const rq = require('request');
rq(process.argv[2]).pipe(fd.createWriteStream(process.argv[3]));
