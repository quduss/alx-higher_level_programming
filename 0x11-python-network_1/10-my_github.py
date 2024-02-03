#!/usr/bin/python3
"""authenticate the user passed as argument to the github api
and fetch the user's id."""


if __name__ == '__main__':
    import sys
    import requests

    url = 'https://api.github.com/user'
    user = sys.argv[1]
    pass_ = sys.argv[2]
    r = requests.get(url, auth=(user, pass_))
    print(r.json().get('id'))
