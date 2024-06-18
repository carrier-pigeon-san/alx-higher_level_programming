#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let instances = 0;
  for (let count = 0; count < list.length; count++) {
    if (list[count] === searchElement) {
      instances += 1;
    }
  }
  return instances;
};
