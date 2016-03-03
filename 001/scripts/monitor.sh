while true;
do
    clear
    date
    echo "redis queue testQueue : $(redis-cli llen testQueue)"
    echo "redis queue logQueue : $(redis-cli llen logQueue)"
    echo "redis queue logInfoQueue : $(redis-cli llen logInfoQueue)"
    echo "mysql testing : $(mysql -uroot -p$1 -e "select count(*) from testing;" --skip-column-names testdb)"
    echo "mysql logInfo : $(mysql -uroot -p$1 -e "select count(*) from logInfo;" --skip-column-names testdb)"
    echo "mongo test : $(mongo --eval "db.test.count()" test)"
    echo "mongo logs : $(mongo --eval "db.logs.count()" test)"

    sleep 1
done
