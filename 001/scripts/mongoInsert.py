import sys
import datetime

from pymongo import MongoClient
connection = MongoClient("mongodb://localhost", w=0)

db=connection.shardTest
test = db.test

tstart = datetime.datetime.now()
d = {'counter' : 0}
amount = 100000
while d['counter'] < amount:
  d['counter'] += 1
  testjs = {"x":d['counter'], "y":"hi" }
  try:
    test.insert(testjs)
  except:
    print "Unexpected error:", sys.exc_info()[0]

tend = datetime.datetime.now()
tdiff = tend - tstart
print tdiff.total_seconds(), 'seconds for ', str(amount), ' records'
