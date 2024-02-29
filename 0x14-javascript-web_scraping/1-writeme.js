#!/usr/bin/node
const fd = require('fs');
fd.writeFile(process.argv[2], process.argv[3], err => {
  if (err) console.log(err);
});
