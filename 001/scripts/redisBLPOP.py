import redis
import time
from datetime import datetime

r_server = redis.Redis('127.0.0.1')

counts = dict()
counter = 0
totaltime = 0
totalcounter = 0
totaltotaltime = 0

while True:
        counter+=1
        start = datetime.now()
        myinfo = r_server.blpop('testQueue', 10)
        #myinfo = r_server.lpop('testQueue', 10)  #test without blocking
        end = datetime.now()
        if not myinfo:
           #if test without blocking, don't break if no info but sleep a little
           break; 
        diff = end - start
        counts[str(diff.microseconds/1000)] = counts.get(str(diff.microseconds/1000), 0) + 1
        totaltime+=diff.microseconds
        if counter==10000:
                print "avg: "+str(totaltime/counter)+" micros"
                print counts
                totalcounter+=counter
                totaltotaltime+=totaltime
                print "totalamount: "+str(totalcounter)+" in avg:"+str(totaltotaltime/totalcounter)+ " micros"
                counter=0
                totaltime=0
                counts.clear()

totalcounter+=counter
totaltotaltime+=totaltime
print "totalamount: "+str(totalcounter)+" in avg:"+str(totaltotaltime/totalcounter)+ " micros"
