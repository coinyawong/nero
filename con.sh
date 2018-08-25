#!/bin/sh
echo "####################################"
echo "1:환경설정, 2: push, 3:pull, 4: DB연결, 5: DB백업"

read -p "명령을 선택 : " a

case $a in
1) ##activate
source yawong_baking/bin/activate;;
2) ## push
git push origin master;;
3) ## pull
git pull origin master;;
4) ## db연결
mysql -u coinyawong2 -p;;
5) ## db백업
mysqldump -u coinyawong2 -p --all-databases > $(date).dump;;
*)
echo "잘못 입력하셨습니다."
esac
