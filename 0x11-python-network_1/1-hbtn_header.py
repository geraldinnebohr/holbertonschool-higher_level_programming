#!/usr/bin/python3
"""Python script that displays the value of the X-Request-Id"""
from urllib import request
import sys


with request.urlopen(sys.argv[1]) as r:
    header_info = r.info()
    print(r.headers['X-Request-Id'])
