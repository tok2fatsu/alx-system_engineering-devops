#!/usr/bin/python3
"""0-subs module"""
import json
import requests

BASE_URL = "https://www.reddit.com/"
HEADERS = {"User-Agent": "ALX_Bot"}


def number_of_subscribers(subreddit):
    """gets the number of subscribers of a subreddit"""
    result = requests.get(
        "{}/{}/about.json".format(BASE_URL, subreddit),
        headers=HEADERS,
        allow_redirects=False,
    )
    if result.status_code == 200:
        data = json.loads(result.text)
        return data["data"]["subscribers"]
    return 0
