#!/usr/bin/python3
"""DOCS"""
import requests


def top_ten(subreddit):
    """Docs"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-agent': 'Mozilla/5.0'}
    params = {'limit': 10}

    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 200:
        for post in response.json().get('data').get('children'):
            print(post.get('data').get('title'))
