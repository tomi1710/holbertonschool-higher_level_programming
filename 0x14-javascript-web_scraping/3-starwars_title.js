#!/usr/bin/node
const request = require('request');
const idpeli = process.argv[2];
const res = 'https://swapi-api.hbtn.io/api/films/' + idpeli;
request(res, function (err, res, body) {
  if (!err) {
    console.log(JSON.parse(body).title);
  } else {
    console.logr(err);
  }
});
