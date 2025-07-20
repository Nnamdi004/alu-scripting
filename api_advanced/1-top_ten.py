#!/usr/bin/python3
"""
This module defines the function `top_ten`.

It queries the Reddit API and prints the titles of the
first 10 hot posts for a given subreddit.
Prints None if the subreddit is invalid.
"""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts of a subreddit.
    If the subreddit is invalid, prints None.

    Args:
        subreddit (str): The subreddit to query.
    """
    if not isinstance(subreddit, str) or subreddit == "":
        print(None)
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "api_advanced:top_ten:v1.0 (by u/alu_student)"
    }
    params = {"limit": 10}

    try:
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get("data", {}).get("children", [])
            for post in data:
                print(post.get("data", {}).get("title"))
        else:
            print(None)
    except requests.RequestException:
        print(None)
