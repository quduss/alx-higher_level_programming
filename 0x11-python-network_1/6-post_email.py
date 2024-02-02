#!/usr/bin/python3
"""post email provided to the url using a POST request via the requests
package"""


if __name__ == '__main__':
    import requests
    import sys
    url = sys.argv[1]
    email = sys.argv[2]
    r = requests.post(url, data={"email": email})
    print(r.text)
