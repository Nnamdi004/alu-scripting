#!/usr/bin/python3
"""
This module defines the function `number_of_subscribers`.

It queries the Reddit API to retrieve the number of subscribers for
a given subreddit. If the subreddit is invalid or inaccessible,
it returns 0.

Usage:
    Call the function with a subreddit name string.
    Example:
        number_of_subscribers('python')

Requirements:
    - requests library
    - A valid User-Agent header to avoid API blocking

Reddit API endpoint used:
    https://www.reddit.com/r/<subreddit>/about.json
"""

import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    Returns 0 if the subreddit is invalid or an error occurs.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers, or 0 if invalid subreddit.
    """
    if not isinstance(subreddit, str) or subreddit == "":
        return 0

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "api_advanced:subscriber.counter:v1.0 (by u/alu_student)"
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            return response.json().get("data", {}).get("subscribers", 0)
        return 0
    except requests.RequestException:
        return 0
