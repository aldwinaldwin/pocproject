import redis
import time
import json
from datetime import datetime
import MySQLdb

r_server = redis.Redis('127.0.0.1')
db = MySQLdb.connect("localhost","root","mypasswd","testdb")
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS logInfo ( path VARCHAR(100), filename VARCHAR(100), amount INT, avgtime FLOAT )")

while True:
        myinfo = r_server.blpop('logInfoQueue', 10)
        if myinfo:
            js = json.loads(myinfo[1])
            try:
                cursor.execute("""INSERT INTO logInfo VALUES (%s,%s,%s,%s)""",(js['path'],js['filename'],js['amount'],js['avgtime']))
                db.commit()
            except:
                db.rollback;
                print "Unexpected error:", sys.exc_info()[0]
        else:
            print "no data"
