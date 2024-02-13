#!/usr/bin/python3
"""
100-count
"""

import requests

def count_words(subreddit, word_list, after=None, counts={}):
    """
    Recursively counts occurrences of words in hot articles of a subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Custom User Agent'}  # Ensure a custom User-Agent header is set
    params = {'limit': 100, 'after': after}

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        posts = data.get('data', {}).get('children', [])
        if posts:
            for post in posts:
                title = post['data']['title'].lower()
                for word in word_list:
                    if word.lower() in title:
                        counts[word.lower()] = counts.get(word.lower(), 0) + 1
            after = data['data']['after']
            if after:
                count_words(subreddit, word_list, after, counts)
            else:
                sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
                for word, count in sorted_counts:
                    print(f"{word}: {count}")
        else:
            return
    else:
        return

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        count_words(sys.argv[1], [x for x in sys.argv[2].split()])
