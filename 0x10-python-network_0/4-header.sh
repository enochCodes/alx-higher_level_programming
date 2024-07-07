#!/bin/bash
# Takes a URL as input, sends a GET request with a header variable X-School-User-Id set to 98, and displays the body of the response
curl -s -H "X-School-User-Id: 98" "$1"
