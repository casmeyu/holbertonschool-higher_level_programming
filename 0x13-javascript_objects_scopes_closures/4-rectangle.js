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

  print () {
    const row = 'X'.repeat(this.width);
    for (let i = 0; i < this.height; i++) {
      console.log(row);
    }
  }

  rotate () {
    const aux = this.width;
    this.width = this.height;
    this.height = aux;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
