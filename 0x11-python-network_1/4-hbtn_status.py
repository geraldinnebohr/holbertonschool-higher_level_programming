#!/usr/bin/python3
"""Python script that fetches an URL"""
import requests


r = requests.get('https://intranet.hbtn.io/status')
content = r.text
t = type(content)
print("Body response:")
print("\t- type:", t)
print("\t- content:", content)
