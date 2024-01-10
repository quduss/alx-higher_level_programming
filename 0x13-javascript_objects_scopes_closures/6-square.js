#!/usr/bin/node

class Square extends require('./5-square.js') {
  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      let shape = '';
      for (let j = 0; j < this.width; j++) {
        if (c) {
          shape += `${c}`;
        } else {
          shape += 'X';
        }
      }
      console.log(shape);
    }
  }
}
module.exports = Square;
