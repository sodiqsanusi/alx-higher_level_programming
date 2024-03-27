#!/bin/bash
# Send a GET request to a URL, with soecified header variables in curl
curl -sL -H "X-School-User-Id: 98" "$1"
