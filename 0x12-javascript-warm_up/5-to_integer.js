#!/usr/bin/node
if (isNaN(process.argv[2])) {
  console.log('Not a number');
} else if (process.argv[2]) {
  console.log('My number: ' + parseInt(process.argv[2], 10));
} else {
  console.log('Not a number');
}
