import praw
import json
import pprint
import sys
import psycopg2


class PsqlConnector():
    def __init__(self, dbname, username, password):
        '''handles the connection'''
        self.dbname = dbname
        self.username = username
        self.password = password

    def connect(self):
        '''handles the variables for the creds'''
        conn = psycopg2.connect(
            #port = 5342, 
            dbname = self.dbname, 
            user = self.username, 
            password = self.password)
        

    def insert():
        '''where we pass the various inserts and select statments'''
        cur = conn.cursor()
        cur.execute("select * from submissions;")
        print ("I worked!")

with open ("/home/hadrian/Documents/psqlcreds.json") as creds:
    '''where we pull the various creds from.'''
    data = json.load(creds)
    dbname = data["dbname"]
    username = data["username"]
    password = data["password"]
import praw
import json
import pprint
import sys
import psycopg2
import Scrapper
scrapper = Scrapper.reddit_scrapper()

class PsqlConnector():
    def __init__(self, dbname, username, password, sub_title, sub_id, sub_score, sub_url, author):
        '''handles the connection'''
        self.dbname = dbname
        self.username = username
        self.password = password
        self.sub_title = sub_title
        self.sub_id = sub_id
        self.sub_score = sub_score
        self.sub_url = sub_url
        self.author = author

    def connect(self):
        '''handles the variables for the creds'''
        conn = psycopg2.connect(
            #port = 5342, 
            dbname = self.dbname, 
            user = self.username, 
            password = self.password)
        

    def insert(self):
        '''where we pass the various inserts and select statments'''
        sub_title = self.sub_title
        sub_id = self.sub_id
        sub_score = self.sub_score
        sub_url = self.sub_url
        author = self.author
        cur = conn.cursor()
        cur.execute("insert into submissions (submission_title, submission_id, submission_score, submission_url, submission_author) values (sub_title, sub_id, sub_score, sub_url, author);")
        print ("I worked!")

with open ("/home/hadrian/Documents/psqlcreds.json") as creds:
    '''where we pull the various creds from.'''
    data = json.load(creds)
    dbname = data["dbname"]
    username = data["username"]
    password = data["password"]


scrapper()
psqlconn = PsqlConnector(dbname, username, password)
psqlconn.connect()
psqlconn.insert()
