#!/usr/bin/python3
""" print the value of X-Request-Id response header after sending
a request to the passed url"""


if __name__ == '__main__':
    import requests
    import sys
    url = sys.argv[1]
    r = requests.get(url)
    print(r.headers['X-Request-Id'])
