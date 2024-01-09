#!/usr/bin/node
const cisfun = 'C is fun';
const x = parseInt(process.argv[2]);

if (!isNaN(x)) {
  for (let j = 0; j < x; j++) {
    console.log(cisfun);
  }
} else {
  console.log('Missing number of occurrences');
}
