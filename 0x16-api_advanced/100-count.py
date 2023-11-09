#!/usr/bin/python3
"""A recursive function that queries the Reddit API,
   parses the title of all hot articles
"""
import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {'limit': 100, 'after': after}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    response = requests.get(url,
                            headers=headers,
                            params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            title = post['data']['title'].lower()
            for word in word_list:
                count = title.count(word)
                if count > 0:
                    if word in word_count:
                        word_count[word] += count
                    else:
                        word_count[word] = count

        new_after = data['data']['after']
        if new_after:
            count_words(subreddit, word_list, new_after, word_count)
        else:
            sorted_word_count = sorted(word_count.items(),
                                       key=lambda x: (-x[1], x[0]))
            for word, count in sorted_word_count:
                print(f"{word}: {count}")
    else:
        return
