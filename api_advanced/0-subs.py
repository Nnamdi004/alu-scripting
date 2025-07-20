#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers
for a given subreddit. Returns 0 if the subreddit is invalid.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Gets the number of subscribers for a subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: Number of subscribers, or 0 if subreddit is invalid.
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
