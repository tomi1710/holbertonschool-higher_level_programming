#!/usr/bin/python3
""" takes your GitHub credentials (username and
    password) and uses the GitHub API to display
    your id """
import requests
import sys

if __name__ == "__main__":
    userxd = sys.argv[1]
    passxd = sys.argv[2]
    link = "https://api.github.com/user"
    res = requests.get(link, auth=(userxd, passxd))
    print(res.json().get('id'))
