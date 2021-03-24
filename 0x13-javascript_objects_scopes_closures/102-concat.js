#!/usr/bin/node
const fs = require('fs');
const first = process.argv[2];
const second = process.argv[3];
const path = process.argv[4];

let alltext = fs.readFileSync(first,
  { encoding: 'utf8', flag: 'r' },
  function (err, data) {
    if (err) { console.log(err); }
  });

  alltext += fs.readFileSync(second,
  { encoding: 'utf8', flag: 'r' },
  function (err, data) {
    if (err) { console.log(err); }
  });

  fs.writeFileSync(path, alltext);
