#!/bin/bash
#Bash script that sends a header variable
 curl -s -o /dev/null -I -w "%{http_code}" "$1"
