#!/bin/bash
# send the request
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
