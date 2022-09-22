#!/bin/bash
#takes in a URL as an argument, sends a GET request tothe URL, and displays the body of the response
curl -s "{$1}" -X GET -H "X-School-User-Id: 98"
