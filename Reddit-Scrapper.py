#All the neccesary imports
import praw
import json
import pprint
import RedditCreds
import sys
import psycopg2
reddit = RedditCreds.reddit_login()

class postings:
    def __init__(self, sub_title, sub_id, sub_score, sub_url, author)
    def scrapper():
        subreddit = reddit.subreddit('politics')
        for submission in reddit.subreddit('politics').new(limit=10):
            #stores all the findings into various variables
            sub_title = submission.title
            sub_id = submission.id
            sub_score = submission.score
            sub_url = submission.url
            author = submission.author
            

    def inserter():
        conn = psycopg2.connect("dbname=root user=postgres")
        cur = conn.cursor()
        cur.execute("select * from submissions;")







