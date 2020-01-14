#!/usr/bin/python3
"""Python script that sends an email as a parameter in a URL"""
import requests
import sys


if __name__ == "__main__":
    r = requests.get('https://swapi.co/api/people/?search=' + sys.argv[1])
    json = r.json()
    results = json['results']
    print('Number of results:', len(results))
    for key in results:
        print(key['name'])
