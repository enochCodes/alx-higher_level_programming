#!/bin/bash
# Sends a GET request to a given URL and displays the body of the response if the status code is 200
curl -sL -w "%{http_code}" "$1" -o /dev/null | grep -q "200" && curl -sL "$1"
