#!/usr/bin/node

exports.esrever = function (list) {
  const list1 = [];
  let j = list.length - 1;

  for (j; j >= 0; j--) {
    list1.push(list[j]);
  }
  return (list1);
};
