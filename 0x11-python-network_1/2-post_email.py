#!/usr/bin/python3
"""Python script that sends an email as a parameter in a URL"""
from urllib import request
from urllib import parse
import sys


encoding = parse.urlencode({'email': sys.argv[2]}).encode('utf-8')
with request.urlopen(sys.argv[1], encoding) as r:
    print(r.read().decode('utf-8'))
