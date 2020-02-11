#!/usr/bin/node
let aux = 0;
exports.logMe = function (item) {
  console.log(aux + ': ' + item);
  ++aux;
};
