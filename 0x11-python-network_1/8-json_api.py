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
        if len(json) == 2:
            print('[{}] {}'.format(json.get('id'), json.get('name')))
        else:
            print('No result')
    except:
        print('Not a valid JSON')
