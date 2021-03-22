#!/usr/bin/node
const str = 'X';
const size = process.argv[2];
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    console.log(str.repeat(size));
  }
}
