#!/usr/bin/python3
"""
1-top_ten
"""

import requests

def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed for a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Custom User Agent'}  # Ensure a custom User-Agent header is set

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        posts = data.get('data', {}).get('children', [])
        if posts:
            for post in posts:
                print(post['data']['title'])
        else:
            print("No posts found for the given subreddit.")
    else:
        print(None)

if __name__ == "__main__":
    top_ten("programming")
