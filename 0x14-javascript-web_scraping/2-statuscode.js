#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response) {
  if (error) {
    console.error('code:', error);
  } else {
    console.log('code:', response && response.statuscode);
  }
});
