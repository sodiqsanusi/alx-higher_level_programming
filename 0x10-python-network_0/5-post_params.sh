#!/bin/bash
# Send POST request to URL, alongside post parameters
curl -s -d "email=test@gmail.com&subject=I will always be here for PLD" "$1" -X POST
