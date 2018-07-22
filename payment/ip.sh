!/bin/sh
echo "위임주소를 입력하세요. :\c"
read AD
echo "닉네임을 입력하세요. :\c"
read name
echo "참여사이클을 입력하세요. :\c"
read cycle
day=$(date)

ad2=`../tezos/tezos-client get manager for $AD`
amount=`../tezos/tezos-client get balance for $AD`

echo $ad2,$amount,$name,$cycle,$day >> t1.txt
