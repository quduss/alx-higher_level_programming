#!/usr/bin/node
const fs = require('fs');

const filePath = process.argv[2];
const content = process.argv[3];

fs.writeFile(filePath, content, 'utf8', function (error) {
  if (error) {
    console.error(error);
  }
});
