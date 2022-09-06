#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.height = w;
      this.width = h;
    }
  }

   print () {
      let i = 0;
      for (i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
   }
};
