#!/usr/bin/node
let big = 0; i = 0; big2 = 0;
const cero = 0;
process.argv.forEach((val, index) => {
  i++;
  if (big < val) {
    big = val;
  }
});
process.argv.forEach((val, index) => {
  if (big2 < val && val !== big) {
    big2 = val;
  }
});
if (i < 3) {
  console.log(cero);
} else {
  console.log(big2);
}
