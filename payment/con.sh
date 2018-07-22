#!/bin/sh
echo "보상사이클을 입력하세요. :\c"
read cycle
echo "수입을 입력하세요. :\c"
read reward
rm -rf con.txt

echo $cycle,$reward >> con.txt

read -p "보상지불을 실시하겠습니까?(예:y, 아니오:n) " b

case $b in
y)
./rd.sh;;
n)
echo "프로세스를 종료합니다.";;
*)
echo "잘못 입력하셨습니다.";;
esac
