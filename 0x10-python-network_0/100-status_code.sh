#!/bin/bash
# Display only the status code of a GET request
curl -s -o /dev/null -I --w '%{http_code}' "$1"
