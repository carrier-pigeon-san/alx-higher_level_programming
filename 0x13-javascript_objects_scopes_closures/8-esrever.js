#!/usr/bin/node
exports.esrever = function (list) {
  let reverse = [];
  for (let count = list.length - 1; count >= 0; count--) {
    reverse = reverse.concat(list[count]);
  }
  return reverse;
};
