import praw
import json
import pprint
import sys
import psycopg2

class PsqlConnector():
    def __init__(self, dbname, username):
        '''handles the connection'''
        self.dbname = dbname
        self.username = username

    def connect(self):
        '''handles the variables for the creds'''
        conn = psycopg2.connect(
            #port = 5342, 
            dbname = self.dbname, 
            user = self.username)
        return conn

dbname = "root"
username = "postgres"

psqlconn = PsqlConnector(dbname, username)
psqlconn.connect()
