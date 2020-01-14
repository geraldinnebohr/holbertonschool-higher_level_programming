#!/usr/bin/python3
"""Python script that sends an email as a parameter in a URL"""
import requests
import sys


if __name__ == "__main__":
    try:
        r = requests.get(sys.argv[1])
        r.raise_for_status()
        print(r.text)
    except:
        print('Error code:', r.status_code)
