#!/usr/bin/node
const fd = require('fs');
fd.readFile(process.argv[2], 'utf8', function (err, cn) {
  console.log(err || cn);
});
