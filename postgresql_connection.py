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
