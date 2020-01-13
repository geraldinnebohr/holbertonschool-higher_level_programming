#!/usr/bin/python3
"""Python script that displays the value of the X-Request-Id"""
import requests
import sys


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers['X-Request-Id'])
