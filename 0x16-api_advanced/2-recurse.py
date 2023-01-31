#!/usr/bin/python3
"""2-recurse
"""
import json

import requests

BASE_URL = "https://www.reddit.com/r"
HEADERS = {"User-Agent": "ALX-Bot"}


def recurse(subreddit, hot_list=[], after=None):
    """recursively traverse all the pages of hot posts of a subreddit and
    return the list of titles
    """
    query = "" if after is None else "?after={}".format(after)
    result = requests.get(
        "{}/{}/hot.json{}".format(BASE_URL, subreddit, query),
        headers=HEADERS,
        allow_redirects=False,
    )

    if result.status_code == 200:
        data = json.loads(result.text)["data"]
        for post in data["children"]:
            hot_list.append(post["data"]["title"])
        after = data["after"]
        return hot_list if after is None else recurse(
            subreddit,
            hot_list,
            after,
        )
    elif len(hot_list) > 0:
        return hot_list
    return None
