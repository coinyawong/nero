#!/bin/sh
echo "####################################"
echo "1:환경설정, 2: 보상지불"

read -p "명령을 선택 : " a

case $a in
1) ##보상사이클 입력
./con.sh;;
2) ##지불
./reward.sh;;
*)
echo "잘못 입력하셨습니다."
esac
