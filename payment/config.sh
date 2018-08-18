#!/bin/sh
echo "보상사이클을 입력하세요. :\c"
read cycle
echo "수입을 입력하세요. :\c"
read reward

roll=`grep $cycle cycle.txt | cut -d , -f2`

rm -rf con.txt
rm -rf cycle.txt

curl http://api.tzscan.io/v2/rolls_history/tz1Zbbuc5Z1ctnCVybqdw7z6FwPjgVufDATc | grep -Po '([0-999999,]+)' | sed ':a;N;$!ba;s/\n/ /g' | sed 's/ , /\n/g' >> cycle.txt


echo $cycle,$reward,$roll >> con.txt

read -p "보상지불을 실시하겠습니까?(예:y, 아니오:n) " b

case $b in
y)
./reward.sh;;
n)
echo "프로세스를 종료합니다.";;
*)
echo "잘못 입력하셨습니다.";;
esac
