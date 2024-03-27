#!/bin/bash
# Display all methods that a server will accept
curl -sI "$1" | grep -i "Allow" | cut -d " " -f2-
