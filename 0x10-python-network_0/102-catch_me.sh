#!/bin/bash
# Make a request to 0.0.0.0:5000/catch_me that causes the server to respond with "You got me!"
curl -s -L -X PUT -d "user_id=98" 0.0.0.0:5000/catch_me
