#!/usr/bin/node

exports.esrever = function (list) {
  const items = [];
  for (let i = list.length - 1; i >= 0; i--) {
    items.push(list[i]);
  }
  return (items);
};
