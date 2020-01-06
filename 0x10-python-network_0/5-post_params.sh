#!/bin/bash
#Bash script that sends a post request
curl "$1" -X POST -sd "email=hr@holbertonschool.com&subject=I will always be here for PLD"
