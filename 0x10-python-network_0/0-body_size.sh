#!/bin/bash

# Check if URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send request
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'

