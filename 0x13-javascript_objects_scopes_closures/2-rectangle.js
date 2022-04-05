#!/usr/bin/node
module.exports = class Rectangle {
  checkNumber (n) {
    return (!isNaN(parseInt(n)));
  }

  constructor (w, h) {
    if (this.checkNumber(w) && this.checkNumber(h)) {
      w = parseInt(w);
      h = parseInt(h);
      if (w > 0 && h > 0) {
        this.width = w;
        this.height = h;
      }
    }
  }
};
