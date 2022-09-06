#!/usr/bin/node
exports.nbocurrences = function (list, searchElement) {
  let i = 0;
  let count = 0;
  for (i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      count++;
    }
  }
  return count;
};
