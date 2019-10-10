import praw
import json
import sys

for p in sys.path:
    print(p)

with open("/home/hlane/Documents/Reddit-Scrapper/creds2", "r") as creds:
    data = json.load(creds)

reddit = praw.Reddit(client_id=data["client_id"],
                     client_secret=data["client_secret"],
                     password=data["password"],
                     user_agent=data["user_agent"],
                     username=data["username"])

print(reddit.user.me())
                     
