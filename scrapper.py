import praw
import RedditCreds

reddit = RedditCreds.reddit_login()

def reddit_scrapper():
    subreddit = reddit.subreddit('politics')
    findings = []
    for submission in reddit.subreddit('politics').new(limit=10):
        sub_title = submission.title
        sub_id = submission.id
        sub_score = submission.score
        sub_url = submission.url
        author = submission.author
        return(sub_title, sub_id, sub_score, sub_url, author)
    
reddit_scrapper()
