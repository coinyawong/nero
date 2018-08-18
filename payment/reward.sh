#!/bin/sh
cycle=`sed -n 1p ./con.txt | cut -d , -f1`
BA=`sed -n 1p ./con.txt | cut -d , -f2`
ROLL=`sed -n 1p ./con.txt | cut -d , -f3`

today=$(date)


cnt=`cat t1.txt|wc -l`

echo "######################################################################"

j=1
while [ $j -le $cnt ]
do
k=`sed -n ${j}p ./t1.txt | cut -d , -f4` ##진입사이클
m=`echo $k+7|bc`
if [ $m -le $cycle ]
then
echo $j"번쨰:" `sed -n ${j}p ./t1.txt | cut -d , -f3`
j=`expr $j + 1`
else
echo $j"번째" `sed -n ${j}p ./t1.txt | cut -d , -f3` "은 이번사이클 대상자가 아닙니다.("$m"사이클 보상예정)"
j=`expr $j + 1`
fi
done

echo "######################################################################"


echo "입금주소를 선택하세요. :\c"
read i


###사이클 정보
k=`sed -n ${i}p ./t1.txt | cut -d , -f4`
m=`echo $k+7|bc`

#### 대상자 검증
if [ $m -gt $cycle ]
then
echo "해당사이클 대상자가 아닙니다."
else

account=`sed -n ${i}p ./t1.txt | cut -d , -f1`
balance=`sed -n ${i}p ./t1.txt | cut -d , -f2`
name=`sed -n ${i}p ./t1.txt | cut -d , -f3`


##수수료&지분
fee=0.055 ## 개별 수정 필요

total=`echo $ROLL*10000|bc -l` ## 롤수

## 5사이클 진입(6롤): 12사이클(18사이클보상)
part=`echo ${balance}/${total}|bc -l`
rd1=`echo ${BA}*${part}|bc`
reward=`echo $rd1 $fee|awk '{printf "%.3f", $1 - $1 * $2}'`
echo "$cycle 번째 사이클, 입금주소: " $account ", 입금대상: " $name ", 입금코인: " $reward
echo "정보가 맞으면 1 아니면 2를 입력하세요:\c"
read ck

if [ ${ck} -eq 1 ]
then
../tezos/tezos-client transfer ${reward} from ledger_coinyawong2_ed to ${account} --fee 0 > payout.out
echo $today $name "님" $cycle "사이클 보상완료 : ../tezos-client transfer ${reward} from ledger_coinyawong2_ed to ${account} --fee 0" >> payout.out
else
echo $name "님 입금이 취소되었습니다." 
fi
fi
