#!/bin/bash
# sends a request to the given url and displays the size of the response body
curl -s "$1" | wc -c
