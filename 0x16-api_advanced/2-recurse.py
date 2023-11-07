#!/usr/bin/python3
"""A recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"after": after}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get("data")
        after = data.get("after")
        posts = data.get("children")

        if not posts:
            return hot_list if hot_list else None

        hot_list.extend([post.get("data").get("title") for post in posts])

        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list if hot_list else None
    else:
        return None
