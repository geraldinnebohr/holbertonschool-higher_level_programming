#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const pattern = 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(pattern.repeat(this.width));
    }
  }

  rotate () {
    const flag = this.width;
    this.width = this.height;
    this.height = flag;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
