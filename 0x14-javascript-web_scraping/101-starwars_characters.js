#!/usr/bin/node
const rq = require('request');
const rul = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
rq(rul, function (err, rp, bd) {
  if (!err) {
    const chr = JSON.parse(bd).characters;
    printCharacters(chr, 0);
  }
});

function printCharacters (chs, idx) {
  rq(chs[idx], function (err, rp, bd) {
    if (!err) {
      console.log(JSON.parse(bd).name);
      if (idx + 1 < chs.length) {
        printCharacters(chs, idx + 1);
      }
    }
  });
}
