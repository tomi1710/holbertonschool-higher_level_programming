#!/usr/bin/node
const argv = process.argv;
let x = 'x';
if (isNaN(argv[2])) {
  console.log('Missing size');
} else {
  for (let j = 0; j < argv[2] - 1; j++) {
    x = x + 'x';
  }
  for (let i = 0; i < argv[2]; i++) {
    console.log(x);
  }
}
