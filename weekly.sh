#!/bin/bash


for (( i = 1; i <= 5; i++ )); do
	num=$(grep -c 'logout' transactionSession/day${i}.txt)
	cat transactionSession/day${i}.txt | ./dailyRun.sh $num
done