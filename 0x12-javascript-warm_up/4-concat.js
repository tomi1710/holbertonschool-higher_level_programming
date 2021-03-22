#!/usr/bin/node
let val1 = 'undefined'; let val2 = 'undefined';
process.argv.forEach((val, index) => {
  if (index === 2) {
    val1 = val;
  }
  if (index === 3) {
    val2 = val;
  }
});
console.log(val1 + ' is ' + val2);
