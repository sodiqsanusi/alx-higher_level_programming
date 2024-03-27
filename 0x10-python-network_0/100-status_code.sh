#!/bin/bash
# Display only the status code of a GET request
curl -sI "$1" | awk '/^HTTP/{print $2}'
