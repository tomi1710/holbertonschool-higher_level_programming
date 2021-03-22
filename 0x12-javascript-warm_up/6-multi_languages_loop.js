#!/usr/bin/node
const object = { a: 'C is fun', b: 'Python is cool', c: 'JavaScript is amazing' };

for (const property in object) {
  console.log(`${object[property]}`);
}
