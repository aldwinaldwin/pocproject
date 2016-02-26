import sys
import datetime
import MySQLdb

#CREATE DATABASE testdb
db = MySQLdb.connect("localhost","root","mypasswd","testdb")
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS testing")

sql = """CREATE TABLE testing ( COL1 INT,COL2 VARCHAR(10) )"""
cursor.execute(sql)

tstart = datetime.datetime.now()
d = {'counter' : 0}
amount = 100000
while d['counter'] < amount:
  d['counter'] += 1
  try:
    cursor.execute("""INSERT INTO testing VALUES (%s,%s)""",(d['counter'],'hi'))
    if d['counter']%1000==0:
        db.commit()
  except:
    db.rollback;
    print "Unexpected error:", sys.exc_info()[0]
db.commit()
tend = datetime.datetime.now()
tdiff = tend - tstart
print tdiff.total_seconds(), 'seconds for ', str(amount), ' records'
