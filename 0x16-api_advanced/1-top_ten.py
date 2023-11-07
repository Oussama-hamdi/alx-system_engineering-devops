#!/usr/bin/python3
"""Queries the Reddit API and prints the titles of the first 10 hot posts"""
import requests


def top_ten(subreddit):
    headers = {"User-Agent": "Mozilla/5.0"}

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    res = requests.get(url, headers=headers, allow_redirects=False)

    if res.status_code != 200:
        print("None")
    else:
        data = res.json().get("data")
        if data:
            children = data.get("children")
            if children:
                for post in children:
                    print(post["data"]["title"])
            else:
                print("None")
