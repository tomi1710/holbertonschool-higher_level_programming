#!/usr/bin/node

exports.converter = function (base) {
  function number (a) {
    return (a.toString(base));
  }
  return (number);
};
