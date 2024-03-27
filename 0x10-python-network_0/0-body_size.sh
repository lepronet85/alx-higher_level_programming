#!/bin/bash
# Fetches the content of the URL provided as argument and displays
# the size of the response body in bytes
curl -s "$1" | wc -c
