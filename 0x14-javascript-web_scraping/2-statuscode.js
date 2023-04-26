#!/usr/bin/node
const fetch = require('fectch');
const url = process.argv[2];

fetch.get(url, (error, response) => {
  if (error) {
    console.log(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
