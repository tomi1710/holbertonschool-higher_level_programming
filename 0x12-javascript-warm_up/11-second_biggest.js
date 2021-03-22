#!/usr/bin/node
let big = 0; let i = 0; let big2 = 0;
const cero = 0;
process.argv.forEach((val, index) => {
  i++;
  if (big / 10 < val / 10) {
    big = val;
  }
});
process.argv.forEach((val, index) => {
  if (big2 / 10 < val / 10 && val / 10 !== big / 10) {
    big2 = val;
  }
});
if (i < 3) {
  console.log(cero);
} else {
  console.log(big2);
}
