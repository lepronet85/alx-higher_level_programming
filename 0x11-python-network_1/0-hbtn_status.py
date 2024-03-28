#!/usr/bin/python3
"""Fetches the status from https://intranet.hbtn.io/status"""
from urllib import request

if __name__ == "__main__":
    with request.urlopen("https://intranet.hbtn.io/status") as response:
        response = response.read()
        print("Response body:")
        print("\t- type: {}".format(type(response)))
        print("\t- content: {}".format(response))
        print("\t- utf8 content: {}".format(response.decode(encoding='utf-8')))
