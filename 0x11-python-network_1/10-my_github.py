#!/usr/bin/python3
"""Python script that sends an email as a parameter in a URL"""
import requests
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    token = sys.argv[2]
    api = 'https://api.github.com/user'

    r = requests.get(api, auth=(user, token))
    json = r.json()
    print(json.get('id'))
