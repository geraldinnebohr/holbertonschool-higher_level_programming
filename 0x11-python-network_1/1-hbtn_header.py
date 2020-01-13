#!/usr/bin/python3
"""Python script that displays the value of the X-Request-Id"""
from urllib import request
import sys


if __name__ == "__main__":
    with request.urlopen(sys.argv[1]) as r:
        print(r.headers['X-Request-Id'])
