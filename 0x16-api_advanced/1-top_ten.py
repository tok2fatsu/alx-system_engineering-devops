#!/usr/bin/python3
"""1-top_ten
"""
import json

import requests

BASE_URL = "https://www.reddit.com/r"
HEADERS = {"User-Agent": "ALX-Bot"}


def top_ten(subreddit):
    """prints the top 10 hot posts of a subreddit"""
    result = requests.get(
        "{}/{}/hot.json?limit=10".format(BASE_URL, subreddit),
        headers=HEADERS,
        allow_redirects=False,
    )
    top_titles = []
    if result.status_code == 200:
        data = json.loads(result.text)
        for post in data["data"]["children"]:
            top_titles.append(post["data"]["title"])

    if len(top_titles) > 0:
        [print(title) for title in top_titles]
    else:
        print(None)
