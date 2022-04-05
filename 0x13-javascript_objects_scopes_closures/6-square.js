#!/usr/bin/node
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c) {
      const row = c.repeat(this.width);
      for (let i = 0; i < this.width; i++) {
        console.log(row);
      }
    } else {
      this.print();
    }
  }
};
