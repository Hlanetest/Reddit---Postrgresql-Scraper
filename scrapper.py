import praw
import RedditCreds
import PsqlConnection

reddit = RedditCreds.reddit_login()

f = PsqlConnection.PsqlConnector('root', 'postgres')
conn = f.connect()
cur = conn.cursor()


    
def reddit_scrapper():
    subreddit = reddit.subreddit('politics')
    for submission in reddit.subreddit('politics').top(limit=120):
        sub_title = submission.title
        sub_id = submission.id
        sub_score = submission.score
        sub_url = submission.url
        author = submission.author
        cur.execute("select * from submissions where submission_id = '{}';".format(sub_id))
        a = cur.fetchone()
        if a is None:
            print (sub_title)
            cur.execute("insert into submissions (submission_title, submission_id, submission_score, submission_url, submission_author) values ({}, '{}', '{}', '{}', '{}');".format(sub_title, sub_id, sub_score, sub_url, author).replace(':', ''))
            print(sub_title)
            print(sub_url)
            conn.commit()
            print("I worked")
        else:
            print (sub_title)
            print("Object already exists")


reddit_scrapper()
