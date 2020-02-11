#!/usr/bin/node
const Square1 = require('./5-square');
class Square extends Square1 {
  charPrint (c) {
    if (typeof c === 'undefined') {
      c = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
