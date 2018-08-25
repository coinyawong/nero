#!/bin/sh
echo "####################################"
echo "1:서버시작, 2: 서버 off,  3: push, 4:pull, 5: DB연결, 6: DB백업"

read -p "명령을 선택 : " a

case $a in
1) ##서버시작
nohup ./yawong_baking/bin/python2.7 ./src/main.py > server.log;;
2) ##서버오프
pkill -9 -ef main.py;;
3) ## push
git push origin master;;
4) ## pull
git pull origin master;;
5) ## db연결
mysql -u coinyawong2 -p;;
6) ## db백업
mysqldump -u coinyawong2 -p --all-databases > $(date +%Y%m%d).dump;;
*)
echo "잘못 입력하셨습니다."
esac
