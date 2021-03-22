#!/usr/bin/node
let big = 0; let i = 0; let big2 = 0;
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
  console.log('0');
} else {
  console.log(big2);
}
