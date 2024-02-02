#!/usr/bin/python3
"""sends a request to the url provided and handle HTTPError
using requests package"""


if __name__ == '__main__':
    import requests
    import sys

    url = sys.argv[1]
    r = requests.get(url)
    try:
        r.raise_for_status()
        print(r.text)
    except requests.exceptions.HTTPError as errh:
        print("Error code: {}".format(r.status_code))
