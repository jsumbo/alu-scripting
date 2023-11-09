#!/usr/bin/python3
"""
This module contains a function to get the number of subscribers of a subreddit.
"""
import requests

def get_number_of_subscribers(subreddit):
    """Returns the number of subscribers or 0 if the subreddit does not exist."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        subscribers = response.json().get('data').get('subscribers')
        if subscribers > 0:
            return "OK"
    return "0"


# Test the function with a specific subreddit
subreddit_name = "learnpython" 
result = get_number_of_subscribers(subreddit_name)
print(result)
