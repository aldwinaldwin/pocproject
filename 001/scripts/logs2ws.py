import requests
import os
import time
from datetime import datetime
import json

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
                requests.post("http://localhost:3000/pushonqueue", data={'queuename': 'logQueue', 'json': json.dumps(js)})
                #r_server.rpush('logQueue',json.dumps(js))
            end = datetime.now()
            diff = end - start
            if counter>0:
                requests.post("http://localhost:3000/pushonqueue", data={'queuename': 'logInfoQueue', 'json': '{"path":"'+dirpath+'","filename":"'+filename+'","amount":"'+str(counter)+'","avgtime":'+str((diff.total_seconds()*1000000+diff.microseconds)/counter)+'}'})
            else:
                requests.post("http://localhost:3000/pushonqueue", data={'queuename': 'logInfoQueue', 'json': '{"path":"'+dirpath+'","filename":"'+filename+'","amount":"'+str(counter)+'","avgtime":0}'})

