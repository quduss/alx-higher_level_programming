#!/bin/bash
# Display all HTTP methods allowed by the server
curl -isX OPTIONS "$1" | grep 'Allow' | cut -d':' -f2 | cut -c 2-
