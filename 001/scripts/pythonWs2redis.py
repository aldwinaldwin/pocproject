#!/usr/bin/env python
import web
import redis

r_server = redis.Redis('127.0.0.1')

urls = (
    '/pushonqueue', 'pushonqueue'
)

app = web.application(urls, globals())

class pushonqueue:
    def POST(self):
        i = web.input()
        r_server.rpush(i.queuename,i.json)
#        print i.queuename+' '+i.json
        return 'OK'

if __name__ == "__main__":
    app.run()
