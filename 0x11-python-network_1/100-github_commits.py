#!/usr/bin/python3
"""Python script that lists list 10 commits (from the most recent
to oldest) of the repository rails"""

import requests
from sys import argv

if __name__ == "__main__":
    url = "https://developer.github.com/v3/repos/commits/?per_page=10"\
    .format(argv[2], argv[1])

    request = requests.get(url)
    commits = request.json()
    for commit in commits:
        print("{}: {}".format(commit.get("sha"),
            commit.get("commit").get("author").get("name")))
