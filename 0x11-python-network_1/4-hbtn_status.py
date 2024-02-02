#!/usr/bin/python3
"""Print some info about the response body after performing
a request to the given url using the requests package"""


if __name__ == '__main__':
    import requests
    url = 'https://alx-intranet.hbtn.io/status'
    r = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
