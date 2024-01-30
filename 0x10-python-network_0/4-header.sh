#!/bin/bash
# Send header variable X-School-User-Id with value of 98 with a GET request to the passed URL
curl -sH "X-School-User-Id: 98" "$1"
