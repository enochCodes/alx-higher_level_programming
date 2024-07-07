#!/bin/bash
# Sends a GET request to a given URL and displays the body of the response if the status code is 200

URL=$1

response=$(curl -s -w "%{http_code}" -o response_body.txt "$URL")
if [ "$response" -eq 200 ]; then
  cat response_body.txt
fi
