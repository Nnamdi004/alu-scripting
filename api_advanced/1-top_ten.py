#!/usr/bin/python3
"""DOCS"""

import requests


def top_ten(subreddit):
    """DOCS"""
    if not isinstance(subreddit, str) or subreddit == "":
        print(None)
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'api_advanced:v1.0 (by u/alu_student)'}
    params = {'limit': 10}

    try:
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 200:
            posts = response.json().get('data', {}).get('children', [])
            for post in posts:
                print(post.get('data', {}).get('title'))
        else:
            print(None)
    except requests.RequestException:
        print(None)
