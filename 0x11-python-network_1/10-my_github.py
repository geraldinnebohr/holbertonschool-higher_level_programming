#!/usr/bin/python3
"""Python script that sends an email as a parameter in a URL"""
import requests
import sys


if __name__ == "__main__":
    r = requests.get('https://api.github.com/users/?client_id=' + sys.argv[1])
    r.add_header('Authorization: token OAUTH-TOKEN')
    json = r.json()
    print(json)
