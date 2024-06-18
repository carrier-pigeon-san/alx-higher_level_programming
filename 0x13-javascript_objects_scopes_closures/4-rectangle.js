#!/usr/bin/node
const { stdout } = require('node:process');

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let c = 0; c < this.height; c++) {
      for (let r = 0; r < this.width; r++) {
        stdout.write('X');
      }
      stdout.write('\n');
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
