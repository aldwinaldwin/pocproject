var express = require('express');
var bodyParser = require('body-parser');
var app = express();
var redis = require("redis"), r_client = redis.createClient();

app.use(bodyParser.urlencoded());

r_client.on("error", function (err) {
        console.log("Redis Error " + err);
});

app.post('/pushonqueue', function (req, res) {
    if(!req.body.hasOwnProperty('queuename') || !req.body.hasOwnProperty('json')) {
        res.statusCode = 400;
        return res.send('Error 400: Post syntax incorrect.');
    }
    r_client.lpush(req.body.queuename, req.body.json);
    res.statusCode = 200;
    return res.send('OK');
});

app.listen(3000, function () {
  console.log('Example app listening on port 3000!');
});

