#!/usr/bin/node
const fetch = require('node-fetch');

const url = process.argv[2];

fetch(url)
  .then(response => {
    console.log(`code: ${response.status}`);
  })
  .catch(error => {
    console.error(error.message);
  });
