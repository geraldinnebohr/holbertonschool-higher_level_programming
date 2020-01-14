#!/usr/bin/python3
"""Python script that sends an email as a parameter in a URL"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 1:
        q = ''
    else:
        q = {'q': sys.argv[1]}
    r = requests.post('http://0.0.0.0:5000/search_user', q)
    try:
        json = r.json()
    except:
        print('Not a valid JSON')
    try:
        print('[{}] {}'.format(json.get('id'), json.get('name')))
    except:
        print('No result')
