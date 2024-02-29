#!/usr/bin/node
const rq = require('request');
rq(process.argv[2], function (err, rp, bd) {
  if (!err) {
    const rl = JSON.parse(bd).results;
    console.log(rl.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  }
});
