import os
import redis
import time
from datetime import datetime
import json

r_server = redis.Redis('127.0.0.1')

for dirpath, dirnames, files in os.walk('/var/log/'):
    print 'treating path: '+dirpath
    for filename in files:
        if filename.endswith('.log'):
            print 'treating file:'+filename
            start = datetime.now()
            fhand = open(dirpath+'/'+filename, 'r')
            counter = 0
            for line in fhand:
                counter += 1
                js = {'path':dirpath,'filename':filename,'log':line}
                r_server.rpush('logQueue',json.dumps(js))
            end = datetime.now()
            diff = end - start
            if counter>0:
                r_server.rpush('logInfoQueue','{"path":"'+dirpath+'","filename":"'+filename+'","amount":"'+str(counter)+'","avgtime":'+str((diff.total_seconds()*1000000+diff.microseconds)/counter)+'}')
            else:
                r_server.rpush('logInfoQueue','{"path":"'+dirpath+'","filename":"'+filename+'","amount":"'+str(counter)+'","avgtime":0}')

