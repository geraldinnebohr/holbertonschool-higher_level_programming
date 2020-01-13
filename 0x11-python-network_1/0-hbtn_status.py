#!/usr/bin/python3
"""Python script that fetches an URL"""
from urllib import request


with request.urlopen('https://intranet.hbtn.io/status') as r:
    url = r.read()
    t = type(url)
    u = url.decode('utf-8')
    print("Body response:")
    print("\t- type:", t)
    print("\t- content:", url)
    print("\t- utf8 content:", u)
