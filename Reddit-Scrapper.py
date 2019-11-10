import praw
import json
import pprint
import sys
import psycopg2




class PsqlConnector():
    def __init__(self, hostname, dbname, username, password):
        '''handles the connection'''
        self.hostname = hostname
        self.dbname = dbname
        self.username = username
        self.password = password

    def connect(self):
        conn = psycopg2.connect(
            hostname = self.hostname,
            port = 5342, 
            dbname = self.dbname, 
            user = self.username, 
            password = self.password)
        

    def insert(self, array):
        cur = conn.cursor()
        cur.execute("insert into submissions ;")

hostname = '127.0.0.1'
dbname = 'root'
username = 'man'
password = 'stuff'



psqlconn = PsqlConnector(hostname, dbname, username, password)
psqlconn.connect()
psqlconn.insert(array)
