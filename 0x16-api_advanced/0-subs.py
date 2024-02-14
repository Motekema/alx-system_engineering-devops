#!/usr/bin/python3
'''
    0-subs
'''
import requests
from sys import argv


def number_of_subscribers(subreddit):
    '''
        Displays the number of subscribers for a given subreddit
    '''
    user = {'User-Agent': 'Lizzie'}
    url = requests.get('https://www.reddit.com/r/{}/about.json'
                       .format(subreddit), headers=user)
    try:
        return url.json().get('data').get('subscribers')
    except Exception:
        return None


if __name__ == "__main__":
    subscribers = number_of_subscribers(argv[1])
    if subscribers is not None:
        print(subscribers)
    else:
        print("OK")
