#!/bin/bash
# Display all methods that a server will accept
curl -s "$1" -X HEAD | grep -i "Allow" | cut -d " " -f2-
