#!/usr/bin/python3
"""Python script that sends an email as a parameter in a URL"""
from urllib import request
from urllib import error
import sys


if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as r:
            print(r.read().decode('utf-8'))
    except error.HTTPError as e:
        print('Error code:', e.code)
