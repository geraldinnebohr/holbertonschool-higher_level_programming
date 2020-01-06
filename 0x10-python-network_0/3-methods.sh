#!/bin/bash
#Bash script that sends a DELETE request to the URL and displays the response
curl -siLX OPTIONS "$1" | grep Allow | cut -d' ' -f2-
