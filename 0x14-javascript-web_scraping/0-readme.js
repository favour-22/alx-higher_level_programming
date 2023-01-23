#!/usr/bin/node
cconst fs = require('fs');

function writeToFile(filePath, stringToWrite) {
  try {
    fs.writeFileSync(filePath, stringToWrite, 'utf8');
  } catch (err) {
    console.error(err);
  }
}

if (process.argv.length === 4) {
  const filePath = process.argv[2];
  const stringToWrite = process.argv[3];
  writeToFile(filePath, stringToWrite);
}
