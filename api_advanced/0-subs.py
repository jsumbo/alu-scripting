#!/usr/bin/python3
"""
This module contains a function to get the number of subscribers of a subreddit.
"""

import requests

def get_number_of_subscribers(subreddit):
    """ returns the number of subscribers """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        subscribers = response.json().get('data').get('subscribers')
        if subscribers > 0:
            return "OK"
    return "0"