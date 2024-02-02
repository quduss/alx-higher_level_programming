#!/usr/bin/python3
"""prints the json response after sending a POST request
to http://0.0.0.0:5000/search_user"""


if __name__ == '__main__':
    import requests
    import sys

    url = 'http://0.0.0.0:5000/search_user'
    try:
        val = sys.argv[1]
    except IndexError:
        val = ""
    r = requests.post(url, data={'q': val})
    try:
        json_response = r.json()
        if json_response == {}:
            print("No result")
        else:
            id_ = json_response.get('id')
            name = json_response.get('name')
            print("[{}] {}".format(id_, name))
    except ValueError:
        print("Not a valid JSON")
