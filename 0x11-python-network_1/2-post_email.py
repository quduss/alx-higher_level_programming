#!/usr/bin/python3
"""sends a post request(email). The url is the first argument
while the email is the second"""


if __name__ == '__main__':
    import urllib.request
    import urllib.parse
    import sys

    url = sys.argv[1]
    value = {'email': sys.argv[2]}
    value = urllib.parse.urlencode(value)
    value = value.encode('ascii')
    req = urllib.request.Request(url, value)
    with urllib.request.urlopen(req) as response:
        content = response.read()
        print(content.decode('utf-8'))
