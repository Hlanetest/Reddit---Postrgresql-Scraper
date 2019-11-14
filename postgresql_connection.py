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
        conn = psycopg2.connect(
            #port = 5342, 
            dbname = self.dbname, 
            user = self.username, 
            password = self.password)
        

    def insert():
        cur = conn.cursor()
        cur.execute("select * from submissions;")
        print ("I worked!")

with open ("/home/hadrian/Documents/psqlcreds.json") as creds:
    data = json.load(creds)
    dbname = data["dbname"]
    username = data["username"]
    password = data["password"]



psqlconn = PsqlConnector(dbname, username, password)
psqlconn.connect()
psqlconn.insert()
