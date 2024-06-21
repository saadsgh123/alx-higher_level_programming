#!/usr/bin/node
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (char = 'X') {
    super.print(char);
  }
}
module.exports = Square;
