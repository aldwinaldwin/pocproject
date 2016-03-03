import redis
import time
import json
from datetime import datetime
from pymongo import MongoClient

r_server = redis.Redis('127.0.0.1')
connection = MongoClient("mongodb://localhost", w=0)

db=connection.test
logs = db.logs


while True:
        myinfo = r_server.blpop('logQueue', 10)
        if myinfo:
            logs.insert(json.loads(myinfo[1]))
        else:
            print "no data"

