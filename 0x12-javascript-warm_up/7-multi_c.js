#!/usr/bin/node
let i;

if (isNaN(process.argv[2])) {
  console.log('Missing number of ocurrences');
} else {
  for (i = 0; i < process.argv[2]; i++) {
    console.log('C is fun');
  }
}
