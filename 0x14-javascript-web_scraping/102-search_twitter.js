#!/usr/bin/node
const enc = require('utf8');
const rq = require('request');
const b64 = require('base-64');

let resp = new Promise(function (resolve, reject) {
  const tk = enc.decode(b64.encode(`${process.argv[2]}:${process.argv[3]}`));
  const ops = {
    url: 'https://api.twitter.com/oauth2/token',
    headers: {
      Authorization: `Basic ${tk}`,
      'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
    },
    form: {
      grant_type: 'client_credentials'
    }
  };
  rq.post(ops, function (error, response, body) {
    if (!error) {
      resolve(JSON.parse(body).access_token);
    }
  });
});

resp.then(
  result => search(result),
  error => console.log(error)
);

function search (bearer) {
  const ops = {
    url: 'https://api.twitter.com/1.1/search/tweets.json',
    headers: {
      Authorization: `Bearer ${bearer}`
    },
    qs: {
      q: process.argv[4],
      count: '5'
    }
  };
  rq.get(ops, function (err, res, bd) {
    if (!err) {
      const posts = JSON.parse(bd).statuses;
      posts.forEach((t) => console.log(`[${t.id}] ${t.text} by ${t.user.name}`));
    }
  });
}
