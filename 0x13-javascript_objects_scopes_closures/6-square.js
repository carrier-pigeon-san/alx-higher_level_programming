#!/usr/bin/node
const { stdout } = require('process');
const Square1 = require('./5-square.js');

class Square extends Square1 {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let char = 'X';
    if (c) {
      char = c;
    }

    for (let r = 0; r < this.height; r++) {
      for (let c = 0; c < this.width; c++) {
        stdout.write(char);
      }
      stdout.write('\n');
    }
  }
}

module.exports = Square;
