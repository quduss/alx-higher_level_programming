#!/usr/bin/node

const arrLength = process.argv.length;

if (arrLength < 4) {
  console.log(0);
} else {
  const arr = [];
  for (let i = 2; i < arrLength - 1; i++) {
    arr[i - 2] = parseInt(process.argv[i]);
  }
  arr.sort();
  for (let i = arr.length - 2; i >= 0; i--) {
    if (arr[i] !== arr[arr.length - 1]) {
      console.log(arr[i]);
      break;
    }
  }
}
