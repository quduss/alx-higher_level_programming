#!/usr/bin/python3
"""Display the body of response in utf-8 after sending
request to the given url. Handle HTTPError exceptions"""


if __name__ == '__main__':
    from urllib.request import Request, urlopen
    from urllib.error import HTTPError
    import sys

    url = sys.argv[1]
    req = Request(url)
    try:
        with urlopen(req) as response:
            content = response.read()
            print(content.decode('utf-8'))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
