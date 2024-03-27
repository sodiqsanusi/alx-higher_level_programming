#!/bin/bash
# Send a DELETE request to a URL, and display its response if successful
curl -s "$1" -X DELETE
