import praw
import json
import pprint
import RedditCreds
import sys

reddit = RedditCreds.reddit_login()


def scrapper():
    subreddit = reddit.subreddit('politics')
    findings = []
    for submission in reddit.subreddit('politics').new(limit=10):
        #print (submission.title)
        findings.append(submission.title)
        findings.append(submission.id)
        findings.append(submission.score)
        findings.append(submission.url)
        findings.append(submission.author)

    for i in range(1, len(findings)):
        return findings

scrapper()



