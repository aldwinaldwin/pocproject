mysql -uroot -p$1 -e "drop table logInfo;" testdb
mysql -uroot -p$1 -e "drop table testing;" testdb
mongo --eval "db.test.drop()" test
mongo --eval "db.logs.drop()" test
redis-cli del testQueue
redis-cli del logQueue
redis-cli del logInfoQueue
