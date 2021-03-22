#!/usr/bin/node
let i = 0;
process.argv.forEach((val, index) => {
  i++;
});
if (i === 2) {
  console.log('No argument');
}
if (i === 3) {
  console.log('Argument found');
}
if (i > 3) {
  console.log('Arguments found');
}
