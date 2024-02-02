#!/usr/bin/python3
"""sends a request to the first argument passed to script
and display the value o the X-Request-Id variable found in the
header of the response"""


if __name__ == '__main__':
    import urllib.request
    import sys
    with urllib.request.urlopen(sys.argv[1]) as resp:
        val = resp.info()['X-Request-Id']
        print(val)
