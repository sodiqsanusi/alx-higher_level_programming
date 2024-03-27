#!/bin/bash
# Send a request to a URL, then display the size of the response body
curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}'
